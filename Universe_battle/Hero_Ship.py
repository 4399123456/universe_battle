import pygame
from Ship import Ship
from settings import Settings

setting = Settings()

class Hero_Ship(Ship):
    def __init__(self,screen,x,y,img_path,life,name):
        super().__init__(screen,x,y,img_path,life,name)
        self.resize_img = pygame.transform.scale(self.sprite_img,setting.hero_size)

    def draw_sprite(self):
        self.screen.blit(self.resize_img,(self.x,self.y))

    def shoot(self,hero_bullet,hero_bullet_group):
        hero_bullet_group.add(hero_bullet)


