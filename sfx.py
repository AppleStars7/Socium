import pygame
import os
pygame.init()
current_path = os.path.dirname(__file__)
sound_path = os.path.join(current_path, "sounds")
startsound = pygame.mixer.Sound(os.path.join(sound_path, "main.wav"))
clearsound = pygame.mixer.Sound(os.path.join(sound_path, "clear.wav"))
endsound =  pygame.mixer.Sound(os.path.join(sound_path, "death.wav"))
stage1sound =  pygame.mixer.Sound(os.path.join(sound_path, "stage1.wav"))
stage2sound =  pygame.mixer.Sound(os.path.join(sound_path, "stage2.wav"))
stage3sound =  pygame.mixer.Sound(os.path.join(sound_path, "stage3.wav"))