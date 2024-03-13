import sys
import pygame
from pygame.locals import *
import game_logic as gl
from Background import Background
from settings import Settings


setting = Settings()
pygame.init()
clock = pygame.time.Clock()

def run_game():
    screen = pygame.display.set_mode((setting.window_width,setting.window_height))
    pygame.display.set_caption(setting.title)
    gl.game_run(screen,clock)


if __name__ == '__main__':
    run_game()

