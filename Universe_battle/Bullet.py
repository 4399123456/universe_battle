import pygame
from settings import Settings

class Bullet(pygame.sprite.Sprite):
    def __init__(self,screen,x,y,img_path):
        super().__init__()
        self.screen = screen
        self.x = x
        self.y = y
        self.img_bullet = pygame.image.load(img_path)
        self.width = self.img_bullet.get_width()
        self.height = self.img_bullet.get_height()
        self.rect = self.img_bullet.get_rect()


    def draw_bullet(self):
        self.screen.blit(self.img_bullet,(self.x,self.y))

    def move_bullet(self,bullet_speed_x,bullet_speed_y):
        self.x += bullet_speed_x
        self.y += bullet_speed_y




