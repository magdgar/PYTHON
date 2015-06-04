import ctypes
import pygame
from game import Game, ServerGame


user32 = ctypes.windll.user32
WIDTH = 600
HEIGHT = 580

pygame.display.set_caption('Pac Man!')
window_surface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

if __name__ == "__main__":
    ServerGame(window_surface)

