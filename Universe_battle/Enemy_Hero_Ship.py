import pygame
from Ship import Ship
from settings import Settings


setting = Settings()

class Enemy_Hero_Ship(Ship):
    def __init__(self,screen,x,y,img_path,life,name):
        super().__init__(screen=screen,x=x,y=y,img_path=img_path,life=life,name=name)

    def shoot(self,enemy_hero_bullet,enemy_hero_bullet_group):
        enemy_hero_bullet_group.add(enemy_hero_bullet)



