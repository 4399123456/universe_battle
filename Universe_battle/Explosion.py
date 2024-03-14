import time
import pygame
from settings import Settings


setting = Settings()
class Explosion(pygame.sprite.Sprite):
    def __init__(self,screen,x,y,images):
        super().__init__()
        self.screen = screen
        self.x = x
        self.y = y
        self.images = images
        self.start_explosion_time = time.time()
        self.explosion_finish = False
        self.frame = 0
        self.load_all_images()

    def load_all_images(self):
        self.imgs = []
        for img in self.images:
            self.imgs.append(pygame.image.load(img))

    def explosion_animation(self):
        end_start_explosion_time = time.time()
        if self.frame <= 8:
            self.screen.blit(self.imgs[self.frame], (self.x, self.y))
        else:
            self.explosion_finish = True
        if end_start_explosion_time - self.start_explosion_time >= setting.explosion_frame:
            self.start_explosion_time = end_start_explosion_time
            self.frame = self.frame + 1



