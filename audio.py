# audio.py

import pygame # type: ignore
import random
from config import STARTUP_SOUND_PATH, SHUTDOWN_SOUND_PATH, SOUND_EFFECTS, VISUALIZE_SOUND_EFFECT

pygame.mixer.init()

def play_startup_sound():
    startup_sound = pygame.mixer.Sound(STARTUP_SOUND_PATH)
    startup_sound.play()

def play_shutdown_sound():
    shutdown_sound = pygame.mixer.Sound(SHUTDOWN_SOUND_PATH)
    shutdown_sound.play()

async def play_random_sound_effect():
    pygame.mixer.init()
    sound_effect = random.choice(SOUND_EFFECTS)
    sound = pygame.mixer.Sound(sound_effect)
    sound.play()
    
async def play_visualize_sound_effect():
    pygame.mixer.init()
    visualize_sound = pygame.mixer.Sound(VISUALIZE_SOUND_EFFECT)
    visualize_sound.play()