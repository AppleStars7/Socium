import os
import pygame
pygame.init()
current_path = os.path.dirname(__file__)
font_path = os.path.join(current_path, "fonts")
game_font = pygame.font.Font(os.path.join(font_path, "Maplestory Bold.ttf"), 15)