import sys
import pygame
from settings import Settings

setting = Settings()

class Health():
    def __init__(self,screen):
        self.screen = screen
        self.Health_bar_x = 10
        self.Health_bar_y = 10
        self.health_bar_img = pygame.image.load(setting.health_bar_path)
        self.blood_width = ((self.health_bar_img.get_width()) / setting.hero_life) - 0.99
        self.blood_height = self.health_bar_img.get_height() - (2 * 3.1)
        self.blood_x = self.Health_bar_x + 3.6
        self.blood_y = self.Health_bar_y + 3.5
        self.hero_life = setting.hero_life

    def draw_health(self):
        # if setting.hero_life > 5:
        #     print(setting.hero_life)
        self.screen.blit(self.health_bar_img,(self.Health_bar_x, self.Health_bar_y))
        for i in range(self.hero_life):
            rects = pygame.rect.Rect(((self.blood_x) + (self.blood_width * i)) + 0.99,self.blood_y,
                                     self.blood_width,self.blood_height)
            pygame.draw.rect(self.screen,setting.blood_color,rects)





