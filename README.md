![Safar Banner](safar.png)
# ** سفر  Safar**

Remember those text adventure games from the 80s? The ones where you'd type "go north" and hope you didn't get eaten by a grue? Well, strap in, because Safar (سفر) is what happens when those games drink a gallon of cosmic coffee and gain sentience!

## 🌌 What in the Universe Is This?

Safar is the text adventure game you've been dreaming about since you first booted up your Commodore 64. It's like someone took the entire cosmos, shrunk it down to fit inside your CLI, and said, "Here, go nuts!"

With Safar, you can:

- 🌟 Watch stars being born (way cooler than watching paint dry)
- 🪐 Visit alien worlds (no green screen required)
- 🧬 Explore the quantum realm (it's like "Honey, I Shrunk the Kids" but sciency)
- 🏙️ Witness historical events (time machine not included)
- 🚀 See future tech (still no flying cars, sorry)
- 🤔 Chat with AI (smarter than your old Magic 8-Ball)
- 🌋 Watch geology happen in real-time (more exciting than it sounds, we promise)
- 🌌 Travel through black holes (no spandex suit needed)

## 🖥️ Features That Would Blow Your 80s Mind

- **Infinite Universe**: More exploration possibilities than you can shake a joystick at
- **Actual Science**: Because "it's magic" is so 1985
- **AI-Generated Images**: Now with options! Choose your flavor of reality-bending visuals
- **Immersive Audio**: Better than the *beep boop* of your old computer
- **Your Choices Matter**: Unlike that "Choose Your Own Adventure" book where all paths led to certain doom

## 🚀 Boarding the Cosmic Express

### Quick Launch (One-Click Installers)

For those who want to jump straight into the cosmic adventure:

1. Clone this repository:
   ```
   git clone https://github.com/fizt656/safar.git
   cd safar
   ```

2. Run the one-click installer for your operating system:
   - On macOS:
     ```
     bash install_safar_mac.sh
     ```
   - On Windows:
     ```
     install_safar_windows.bat
     ```

These scripts will:
- Set up a virtual environment
- Install all required dependencies
- Create a `config.py` file from the example
- Prompt you for your OpenRouter API key and Replicate API token
- Configure the environment variables with your API keys

After installation, follow the on-screen instructions to activate the virtual environment and launch Safar.

### Running Safar

After installation, run Safar using these commands:

- On macOS and Linux:
  ```
  source safar_env/bin/activate
  python safar.py
  ```

- On Windows:
  ```
  safar_env\Scripts\activate.bat
  python safar.py
  ```

### Updating API Keys

If you need to update your API keys in the future, you have two options:

1. Edit the `config.py` file:
   - Open the `config.py` file in a text editor.
   - Update the `OPENROUTER_KEY` and/or `REPLICATE_API_TOKEN` values.
   - Save the file and restart Safar.

2. Set environment variables:
   - Set the `OPENROUTER_KEY` and `REPLICATE_API_TOKEN` environment variables before running Safar.
   - These will override the values in `config.py`.

### Manual Installation

If you prefer to have more control over the installation process:

1. Clone this bad boy:
   ```
   git clone https://github.com/fizt656/safar.git
   cd safar
   ```

2. Create a virtual environment (because we're not savages):
   ```
   python -m venv safar_env
   ```

3. Activate your shiny new environment:
   - On Windows:
     ```
     safar_env\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source safar_env/bin/activate
     ```

4. Install the future:
   ```
   pip install -r requirements.txt
   ```

5. Set up your cosmic keys:
   - Copy `config_example.py` to `config.py`
   - Edit `config.py` and add your OpenRouter API key and Replicate API token, or set them as environment variables

6. Launch into the unknown:
   ```
   python safar.py
   ```

7. To return to boring old reality (why would you?), deactivate the virtual environment:
   ```
   deactivate
   ```

## 🕹️ How to Play (No Cartridge Blowing Required)
Type whatever your heart desires. "Go north" is so passé. You can do it, sure... but you can really do anything.  Try all sorts of stuff.  Watch galaxies being born.  Or, zoom in on some dude mowing his lawn on an average day.  Whatever you want really.


## 🕹️ Commands

- **Visualize**: Type 'visualize' to see what this cosmic madness looks like.
- **Rage Quit**: Just kidding, type 'quit' to exit (but why would you?).

## 🎨 Choose Your Reality Painter

- **Replicate API**: For when you want your cosmic visions served fresh from the cloud. Perfect for those who like their realities with a side of internet.
- **Local Stable Diffusion**: Keep your hallucinations close to home. Ideal for the "I don't trust the cloud with my interdimensional travel plans" crowd.

## 🤝 Join the Cosmic Crew

Got ideas? Bugs? A theory about the meaning of life? We want it all! Contribute and become part of the Safar legend.

## 📜 Legal Stuff

This project is under a dual license. See [LICENSE](LICENSE) for details. (It's way more fun than the legal text in your old game manuals.)

## 🙏 Tip of the Space Helmet
- Every sci-fi author, mad scientist, and daydreamer who made us believe in the impossible