![Safar Banner](safar.png)
# ** سفر Safar: Desert Reverie **

Remember those text adventure games from the 80s? The ones where you'd type "go east" and hope you didn't fall into a bottomless pit? Well, get ready for a sand-tastic adventure, because Safar: Desert Reverie is what happens when those games drink a gallon of magic lamp oil and gain sentience!

## �️ What in the Desert Is This?

Safar: Desert Reverie is the text adventure game you've been dreaming about since you first booted up your Commodore 64. It's like someone took the entire Arabian Nights, shrunk it down to fit inside your CLI, and said, "Here, go nuts!"

With Safar: Desert Reverie, you can:

- 🌟 Explore mystical oases (way cooler than watching sand blow)
- � Encounter mischievous genies (no green screen required)
- 🏺 Uncover ancient artifacts (it's like "Aladdin" but you're the star)
- � Discover hidden desert cities (magic carpet not included)
- � Lead a camel caravan (still no flying carpets, sorry)
- 🤔 Solve cryptic riddles (smarter than your old Magic 8-Ball)
- 🌋 Brave scorching deserts and treacherous canyons (more exciting than it sounds, we promise)
- � Navigate by the desert stars (no GPS needed)

## 🖥️ Features That Would Blow Your 80s Turban Off

- **Endless Desert**: More exploration possibilities than you can shake a snake charmer's flute at
- **Mystical Magic**: Because "it's science" is so 2085
- **AI-Generated Images**: Now with options! Choose your flavor of sand-bending visuals
- **Immersive Audio**: Better than the *beep boop* of your old computer, now with continuous desert ambiance!
- **Your Choices Matter**: Unlike that "Choose Your Own Adventure" book where all paths led to dehydration

## � Mounting Your Digital Camel

### Quick Launch (One-Click Installers)

For those who want to jump straight into the desert adventure:

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

After installation, follow the on-screen instructions to activate the virtual environment and launch Safar: Desert Reverie.

### Running Safar: Desert Reverie

After installation, run Safar: Desert Reverie using these commands:

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
   - Save the file and restart Safar: Desert Reverie.

2. Set environment variables:
   - Set the `OPENROUTER_KEY` and `REPLICATE_API_TOKEN` environment variables before running Safar: Desert Reverie.
   - These will override the values in `config.py`.

### Manual Installation

If you prefer to have more control over the installation process:

1. Clone this magic lamp:
   ```
   git clone https://github.com/fizt656/safar.git
   cd safar
   ```

2. Create a virtual environment (because we're not desert wanderers):
   ```
   python -m venv safar_env
   ```

3. Activate your shiny new oasis:
   - On Windows:
     ```
     safar_env\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source safar_env/bin/activate
     ```

4. Install the mystical packages:
   ```
   pip install -r requirements.txt
   ```

5. Set up your magical keys:
   - Copy `config_example.py` to `config.py`
   - Edit `config.py` and add your OpenRouter API key and Replicate API token, or set them as environment variables

6. Launch into the unknown desert:
   ```
   python safar.py
   ```

7. To return to boring old reality (why would you?), deactivate the virtual environment:
   ```
   deactivate
   ```

## 🕹️ How to Play (No Sand Clearing Required)
Type whatever your heart desires. "Go east" is so passé. You can do it, sure... but you can really do anything. Try all sorts of stuff. Haggle with merchants in bustling bazaars. Seek the wisdom of ancient desert sages. Or, zoom in on some guy tending his date palm orchard on an average day. Whatever you want really.

## 🕹️ Commands and Controls

- **Visualize**: 
  - Type 'vis' or 'visualize' to see a full, immersive visualization of your desert adventure. This includes all the pixelated graphical stuff and dramatic CLI effects.
  - Type 'visfast' for a quick visualization that generates and opens the image as fast as a genie can grant wishes.
- **Pause Menu**: Press the 'Esc' key to bring up the pause menu. From here, you can:
  - Resume the game
  - Exit to the main menu
  - Exit the game entirely
- **Options**: Access the options menu to adjust settings like image generation method and music volume.
- **Rage Quit**: Just kidding, type 'quit' to exit (but why would you leave this magical realm?).

## 🎨 Choose Your Mirage Painter

- **Replicate API**: For when you want your desert visions served fresh from the cloud. Perfect for those who like their mirages with a side of internet.
- **Local Stable Diffusion**: Keep your hallucinations close to home. Ideal for the "I don't trust the cloud with my interdimensional sand castle" crowd.

## 🤝 Join the Caravan Crew

Got ideas? Bugs? A theory about the meaning of desert life? We want it all! Contribute and become part of the Safar: Desert Reverie legend.

## 📜 Legal Stuff

This project is under a dual license. See [LICENSE](LICENSE) for details. (It's way more fun than the legal text in your old game manuals.)

## 🙏 Tip of the Fez
- Every fantasy author, mad wizard, and daydreamer who made us believe in the magic of the desert