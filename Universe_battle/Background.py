import sys
import pygame
from settings import Settings

setting = Settings()

class Background():
    def __init__(self,screen):
        self.screen = screen
        self.width = 1200
        self.height = 600
        self.img = pygame.image.load(setting.bg_path)
        self.x1 = 0
        self.x2 = self.width
        self.y1 = 0
        self.y2 = 0

    def draw(self):
        self.screen.blit(self.img,(self.x1,self.y1))
        self.screen.blit(self.img,(self.x2,self.y2))

    def move(self):
        self.x1 -= setting.bg_speed
        self.x2 -= setting.bg_speed
        if self.x1 <= -self.width:
            self.x1 = 0
        if self.x2 <= 0:
            self.x2 = self.width

