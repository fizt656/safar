# safar.py

import asyncio
import os
import subprocess
import sys
from api import generate_response, generate_image_prompt, generate_image
from utils import print_slow, print_slow_multiline, print_progress_bar, print_warning_bar
from audio import play_startup_sound, play_shutdown_sound, play_random_sound_effect, play_visualize_sound_effect
from config import (
    IMAGE_DIRECTORY, TerminalColors, BANNER, GOODBYE_BANNER, VISUALIZE_SOUND_EFFECT,
    check_and_update_api_key, check_and_update_replicate_token, set_image_gen_method
)

def open_file(file_path):
    if sys.platform.startswith('darwin'):  # macOS
        subprocess.run(['open', file_path])
    elif sys.platform.startswith('win32'):  # Windows
        os.startfile(file_path)
    else:  # Linux and other Unix-like
        subprocess.run(['xdg-open', file_path])

def choose_image_generation_method():
    while True:
        choice = input("Choose image generation method (1 for Replicate API, 2 for local Stable Diffusion): ").strip()
        if choice == '1':
            return 'replicate'
        elif choice == '2':
            return 'local_sd'
        else:
            print("Invalid choice. Please enter 1 or 2.")

async def main():
    # Choose image generation method
    method = choose_image_generation_method()
    set_image_gen_method(method)

    # Check and update the API keys if necessary
    api_key = check_and_update_api_key()
    if method == 'replicate':
        replicate_token = check_and_update_replicate_token()

    play_startup_sound()
    await print_slow_multiline(f"""Initializing Safar...{TerminalColors.OKGREEN}█▓░█▓░█▓░█▓▓░{TerminalColors.ENDC}
Loading Core Modules... {TerminalColors.OKGREEN}█▓░█▓░█▓░█▓▓░{TerminalColors.ENDC}
Verifying System Integrity...{TerminalColors.OKGREEN}█▓░█▓░█▓░█▓▓░{TerminalColors.ENDC}
""")
    await print_slow_multiline(BANNER)
    await print_slow_multiline(f"{TerminalColors.OKBLUE}Initiating quantum core startup...{TerminalColors.ENDC}")
    await print_warning_bar(duration=1)

    await print_slow_multiline(f"{TerminalColors.HEADER}Decrypting celestial payload...{TerminalColors.ENDC}")
    await print_warning_bar(duration=2.5)

    await print_slow(f"{TerminalColors.OKBLUE}|*!!DATA DECRYPTED!!*|{TerminalColors.ENDC}")
    await print_slow("Star clusters aligned: 8472")
    await print_slow("Quantum flux stability: 97.3%")
    await print_slow("Nebula gas index: 44.8")

    await print_slow("Loading complete.")
    print(f"{TerminalColors.OKBLUE}Safar {TerminalColors.OKGREEN} Universe Matrix {TerminalColors.ENDC}[v. ῳnπ]")
    print("Last celestial insertion: ♎︎13,799,700,012.7")
    print()

    conversation_history = []

    while True:
        user_input = input(f"{TerminalColors.OKGREEN}$Safar>{TerminalColors.ENDC}")

        if user_input.lower() == 'quit':
            play_shutdown_sound()
            await print_slow("Last celestial evacuation: ♎︎13,799,700,012.7")
            await print_slow(f"{TerminalColors.WARNING}Initiating quantum core quench sequence...{TerminalColors.ENDC}")
            await print_warning_bar(duration=0.5)
            await print_slow_multiline(GOODBYE_BANNER, delay=0.015)
            break

        if user_input.lower() == 'visualize':
            await play_visualize_sound_effect()  # Play the visualization sound effect

            if len(conversation_history) > 0:
                last_message = conversation_history[-1][1]  # Get the last assistant's message

                context = f"""Based on the following text adventure context:\n{last_message}\n\nGenerate a detailed image prompt for an AI image generation model to create an image that captures the player's surroundings, objects, characters, and any other relevant visual elements mentioned in the context. The prompt should provide a comprehensive description of what the player is seeing from their point of view (POV) in the text adventure."""

                image_prompt = await generate_image_prompt(context)
                if image_prompt:
                    # Start the image generation process concurrently
                    image_generation_task = asyncio.create_task(generate_image(image_prompt))

                    # Display progress bars and status updates while the image is being generated
                    await print_slow_multiline(f"""Initializing Quantum Visualization Core...{TerminalColors.WARNING}█▓░█▓░█▓░█▓▓░{TerminalColors.ENDC}
        Loading Core Modules... {TerminalColors.WARNING}█▓░█▓░█▓░█▓▓░{TerminalColors.ENDC}
        Verifying Visualization Integrity...{TerminalColors.WARNING}█▓░█▓░█▓░█▓▓░{TerminalColors.ENDC}
        """, delay=.008)        
                    api_name = "Replicate API" if method == 'replicate' else "Local Stable Diffusion"
                    await print_slow_multiline(f"{TerminalColors.OKBLUE}Initializing {api_name} Connection...{TerminalColors.ENDC}")
                    await print_warning_bar(duration=6)
                    await print_slow_multiline(f"{TerminalColors.HEADER}Processing Image Generation...{TerminalColors.ENDC}")
                    await print_warning_bar(duration=5)
                    await print_slow(f"{api_name} {TerminalColors.OKGREEN}Connected: 8472{TerminalColors.ENDC}")
                    await print_slow(f"Quantum seed stability: {TerminalColors.OKGREEN}97.3%{TerminalColors.ENDC}")
                    await print_slow(f"Image Resolution Index: {TerminalColors.OKGREEN}44.8{TerminalColors.ENDC}")
                    await print_slow(f"Generation Parameters Set: {TerminalColors.OKGREEN}74.625{TerminalColors.ENDC}")
                    await print_slow(f"{api_name} {TerminalColors.OKGREEN}ACTIVATED{TerminalColors.ENDC}")
                    await print_slow(f"{TerminalColors.WARNING}Rendering output.................................. ")
                    await print_warning_bar(duration=5)

                    # Wait for the image generation to complete
                    image_path = await image_generation_task
                    
                    if image_path:
                        await print_slow_multiline(f"{TerminalColors.WARNING}Initializing quantum upscaler....................... {TerminalColors.WARNING}Initialized =======>>>>> Image Rendered********{TerminalColors.HEADER}>>>>>>>>>>>>>>>>>SENT TO WARP-MAIL{TerminalColors.ENDC}",delay=.025)
                        await print_slow_multiline(f"\n{TerminalColors.OKBLUE}Image prompt sent to {api_name}:{TerminalColors.ENDC}")
                        await print_slow_multiline(f"{TerminalColors.OKGREEN}{image_prompt}{TerminalColors.ENDC}\n")
                        print(f"[Image generated: {image_path}]")
                        open_file(image_path)
                    else:
                        print("[Error generating image]")
                else:
                    print("[Error generating image prompt]")
            else:
                print("[No previous context available for visualization]")
            
        else:
            conversation_history.append(("user", user_input))
            await print_slow_multiline(f"{TerminalColors.HEADER}Processing your request...{TerminalColors.ENDC}")
            await play_random_sound_effect()  # Play a random sound effect for general input
            response = await generate_response(conversation_history, 'openrouter', api_key)  # Use the updated api_key
            conversation_history.append(("assistant", response))
            print()

if __name__ == "__main__":
    asyncio.run(main())