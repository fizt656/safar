import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import asyncio
import os
from config import GAME_TITLE, WINDOW_SIZE, TEXT_COLOR_PLAYER_INPUT, TEXT_COLOR_GAME_RESPONSE, MAX_CONVERSATION_HISTORY, BANNER, set_image_gen_method
from safar import Safar

class SafarGUI:
    def __init__(self, master):
        self.master = master
        master.title(GAME_TITLE)
        master.geometry(WINDOW_SIZE)
        master.configure(bg='black')

        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure('TFrame', background='black')
        self.style.configure('TButton', background='#333333', foreground='white')
        self.style.configure('TLabel', background='black', foreground='white')
        self.style.configure('TEntry', fieldbackground='#333333', foreground='white')

        self.safar = Safar()
        self.create_main_menu()

    def create_main_menu(self):
        self.main_menu_frame = ttk.Frame(self.master, padding="10")
        self.main_menu_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        # Load, crop, scale, and display the banner image
        banner_image = Image.open("safar.png")
        banner_image = self.crop_center(banner_image, 4/3)
        banner_image = banner_image.resize((600, 450), Image.LANCZOS)  # Adjust size as needed
        banner_photo = ImageTk.PhotoImage(banner_image)
        banner_label = ttk.Label(self.main_menu_frame, image=banner_photo)
        banner_label.image = banner_photo
        banner_label.grid(row=0, column=0, columnspan=2, pady=20)

        start_button = ttk.Button(self.main_menu_frame, text="START GAME", command=self.start_game)
        start_button.grid(row=1, column=0, columnspan=2, pady=10)

        options_button = ttk.Button(self.main_menu_frame, text="OPTIONS", command=self.show_options)
        options_button.grid(row=2, column=0, columnspan=2, pady=10)

    def crop_center(self, image, aspect_ratio):
        width, height = image.size
        new_width = min(width, int(height * aspect_ratio))
        new_height = min(height, int(width / aspect_ratio))
        left = (width - new_width) / 2
        top = (height - new_height) / 2
        right = (width + new_width) / 2
        bottom = (height + new_height) / 2
        return image.crop((left, top, right, bottom))

    def show_options(self):
        options_window = tk.Toplevel(self.master)
        options_window.title("Options")
        options_window.geometry("300x200")
        options_window.configure(bg='black')

        ttk.Label(options_window, text="Choose Image Generation Method:").pack(pady=10)

        method_var = tk.StringVar()
        replicate_radio = ttk.Radiobutton(options_window, text="Replicate", variable=method_var, value="replicate")
        replicate_radio.pack()
        local_sd_radio = ttk.Radiobutton(options_window, text="Local Stable Diffusion", variable=method_var, value="local_sd")
        local_sd_radio.pack()

        def save_options():
            chosen_method = method_var.get()
            if chosen_method:
                set_image_gen_method(chosen_method)
                options_window.destroy()

        save_button = ttk.Button(options_window, text="Save", command=save_options)
        save_button.pack(pady=20)

    def start_game(self):
        self.main_menu_frame.destroy()
        self.create_game_widgets()
        self.stream_intro_text()

    def create_game_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        # Game output text area
        self.game_text = tk.Text(main_frame, wrap=tk.WORD, width=80, height=20, bg='black', fg='white')
        self.game_text.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.game_text.config(state=tk.DISABLED)

        # Configure text colors
        self.game_text.tag_configure("player_input", foreground=TEXT_COLOR_PLAYER_INPUT)
        self.game_text.tag_configure("game_response", foreground=TEXT_COLOR_GAME_RESPONSE)

        # Scrollbar for game text
        text_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.game_text.yview)
        text_scrollbar.grid(row=0, column=2, sticky=(tk.N, tk.S))
        self.game_text['yscrollcommand'] = text_scrollbar.set

        # Input field
        self.input_field = ttk.Entry(main_frame, width=70)
        self.input_field.grid(row=1, column=0, sticky=(tk.W, tk.E))
        self.input_field.bind("<Return>", lambda event: self.process_input())

        # Submit button
        submit_button = ttk.Button(main_frame, text="Submit", command=self.process_input)
        submit_button.grid(row=1, column=1, sticky=tk.E)

        # Image display area
        self.image_label = ttk.Label(main_frame)
        self.image_label.grid(row=2, column=0, columnspan=2, pady=10)

        # Configure grid weights
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)

    def stream_intro_text(self):
        intro_text = self.safar.start()
        self.stream_text(intro_text, "game_response")

    def stream_text(self, text, tag):
        def stream(remaining_text):
            if remaining_text:
                self.update_game_text(remaining_text[0], tag)
                self.master.after(10, lambda: stream(remaining_text[1:]))
            else:
                self.input_field.focus_set()

        stream(text)

    def process_input(self):
        user_input = self.input_field.get()
        self.input_field.delete(0, tk.END)

        if user_input.lower() == 'quit':
            shutdown_message = self.safar.shutdown()
            self.stream_text(shutdown_message, "game_response")
            self.master.after(3000, self.master.quit)  # Close the window after 3 seconds
        else:
            self.update_game_text(f"> {user_input}\n", "player_input")
            self.master.after(0, self.async_process_command, user_input)

    def async_process_command(self, command):
        asyncio.run(self.process_command(command))

    async def process_command(self, command):
        response = await self.safar.process_input(command)
        if isinstance(response, str):
            # For visualization commands or error messages that return a string
            self.stream_text(response, "game_response")
            if "Image generated:" in response or "Quick visualization generated:" in response:
                image_path = response.split(":")[1].split("\n")[0].strip()
                self.display_image(image_path)
        else:
            # For normal responses that are streamed
            async for token in response:
                self.update_game_text(token, "game_response")
                await asyncio.sleep(0.01)  # Small delay to allow GUI to update

    def update_game_text(self, text, tag):
        self.game_text.config(state=tk.NORMAL)
        self.game_text.insert(tk.END, text, tag)
        self.game_text.see(tk.END)
        self.game_text.config(state=tk.DISABLED)
        self.master.update_idletasks()  # Force GUI update

    def display_image(self, image_path):
        if image_path and os.path.exists(image_path):
            try:
                image = Image.open(image_path)
                image = image.resize((400, 300), Image.LANCZOS)  # Adjust size as needed
                photo = ImageTk.PhotoImage(image)
                self.image_label.config(image=photo)
                self.image_label.image = photo
            except Exception as e:
                self.update_game_text(f"Error displaying image: {str(e)}\n", "game_response")
        else:
            self.update_game_text(f"Error: Image file not found or generation failed\n", "game_response")

if __name__ == "__main__":
    root = tk.Tk()
    game = SafarGUI(root)
    root.mainloop()