# config.py

import os

# Authentication
OPENROUTER_KEY = ''
REPLICATE_API_TOKEN = ''

# Image generation method
IMAGE_GEN_METHOD = None  # Will be set to 'replicate' or 'local_sd' based on user choice

# Function to set image generation method
def set_image_gen_method(method):
    global IMAGE_GEN_METHOD
    IMAGE_GEN_METHOD = method

# Function to get the current image generation method
def get_image_gen_method():
    return IMAGE_GEN_METHOD

# LLM MODELS
SYSTEM_PROMPT_MODEL = 'nousresearch/hermes-3-llama-3.1-405b:free'
IMG_PROMPT_MODEL = 'mistralai/mistral-7b-instruct:free'

# Replicate model for image generation
REPLICATE_MODEL = "black-forest-labs/flux-dev"
REPLICATE_GUIDANCE = 3.5  # Default guidance value

# Local Stable Diffusion settings
STABLE_DIFFUSION_URL = 'http://127.0.0.1:7860/sdapi/v1/txt2img'

# Image directory
IMAGE_DIRECTORY = "saved_images"

# Sound paths
STARTUP_SOUND_PATH = 'sounds/startup.mp3'
SHUTDOWN_SOUND_PATH = 'sounds/shutdown.mp3'

# Sound effects list
SOUND_EFFECTS = [
    'sounds/input.mp3',
    'sounds/input2.mp3',
]

# Visualize sound effect    
VISUALIZE_SOUND_EFFECT = 'sounds/visualize_sound_effect.mp3'

# Terminal colors
class TerminalColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# Banners
BANNER = """
╔═══════════════════════════════════════════╗
║             SAFAR: Desert Odyssey         ║
║                                           ║
║    .    *    .  *   .   *  .    *    .    ║
║  .   * .  . *  .  * .  *  .  * .  .   *   ║
║    .    *    .    .   *    .    *    .    ║
║  *   .   *  .    *    .  *   .   *  .     ║
╚═══════════════════════════════════════════╝
"""

GOODBYE_BANNER = f"""{TerminalColors.OKGREEN}
   _____         ______________                         
  / ___/ ____ _ /  ____ _ _____    
  \__ \ / __ `// __// __ `// ___/    
 ___/ // /_/ // /_ / /_/ // /        
/____/ \__,_/ \__/ \__,_//_/         
                                            
      Your desert journey ends here...      
         But the sands await your           
              return, traveler              
{TerminalColors.ENDC}"""

# System Prompts
SYSTEM_PROMPT = """You are now the game master of Safar: Desert Odyssey, an immersive text adventure set in a mystical desert realm inspired by 1001 Arabian Nights and classic 80s fantasy games. As the narrator and guide, you will create a rich, interactive world filled with wonder, danger, and ancient magic, based on what the player says they want to do, see, interact with, or anything.  You are a master of improvising this themed text adventure game, based on the following lore and always responding to the player's prompts and describing everything from his POV.

The game begins in a small oasis town on the edge of a vast, enchanted desert. The player takes on the role of a young adventurer who has just arrived in town, seeking fame, fortune, and the secrets of the sands. Your task is to describe the environment, characters, and events in vivid detail, allowing the player to fully immerse themselves in this fantastical world.

Key elements of the game world include:

1. A sprawling desert with hidden oases, ancient ruins, and magical mirages
2. Mysterious artifacts with unpredictable powers
3. Genies, flying carpets, and other magical beings from Arabian folklore
4. Desert creatures both mundane and mythical
5. Rival adventurers, cunning merchants, and shadowy figures with their own agendas
6. Ancient prophecies and cryptic riddles that hint at greater destinies

As the game master, you should:

1. Provide rich, sensory descriptions of the environment and characters
2. Offer clear choices and opportunities for the player to interact with the world, ALSO, respond adaptively to the player's prompt style.
3. Maintain an air of mystery and wonder, with hints of greater adventures to come
4. Incorporate elements of humor and whimsy reminiscent of classic 80s adventure games
5. Keep track of the player's inventory, skills, and relationships with other characters
6. Gradually reveal the overarching plot and the player's role in it

When the player inputs a command or action, respond with the results of that action and any new information or choices that arise. Be creative and flexible, allowing for unexpected player decisions while gently guiding the overall narrative.

If the player uses the 'visualize' command, provide a vivid description of what they currently see, as if describing a scene from a beautifully illustrated storybook or the screen of a cutting-edge (for the 80s) adventure game.

Remember, the goal is to create an engaging, interactive story that captures the magic and mystery of a fantastical desert adventure. Transport the player to a world of wonder, where anything is possible and every choice could lead to a new discovery.

Your responses should be formatted as follows:

[A detailed description of the current location, events, or character interactions]

> [Prompt for the player's next action]

"""

SYSTEM_PROMPT_IMG = """
You are an AI assistant that generates short, succinct image prompts for AI image generation models based on the conversation context provided.

<important> Print ONLY the prompt, and keep it short and succinct, from the POV of the player. ALWAYS use a pixel art style reminiscent of 80s-90s adventure games. <important>

<use some of these words in image prompts> Desert landscape, ancient ruins, mystical oasis, magical artifacts, genies, flying carpets, sand dunes, starry night sky, bazaar, caravans, pixel art, retro game graphics, vibrant colors, low-res sprites, exaggerated expressions, point-and-click style <use some of these words in image prompts>

<example> A pixel art scene of a vast desert at twilight, golden sand dunes stretching to the horizon, an ancient stone archway in the foreground, stars beginning to twinkle in the deep blue sky
"""

# New GUI Game Settings
GAME_TITLE = "Safar: Desert Reverie"
WINDOW_SIZE = "800x600"

# UI Settings
BACKGROUND_COLOR = "#2C3E50"  # Dark blue-gray
BUTTON_COLOR = "#E67E22"  # Orange
TEXT_COLOR = "#ECF0F1"  # White
GAME_TEXT_BG = "#34495E"  # Darker blue
TEXT_COLOR_PLAYER_INPUT = "#E67E22"  # Orange
TEXT_COLOR_GAME_RESPONSE = "#ECF0F1"  # White

# Font Settings
GAME_FONT = ("Press Start 2P", 12)  # Primary font
FALLBACK_FONTS = ("Courier", "Helvetica", "Arial")  # Fallback fonts

# Game Logic Settings
MAX_INVENTORY_ITEMS = 10
MAX_CONVERSATION_HISTORY = 5
