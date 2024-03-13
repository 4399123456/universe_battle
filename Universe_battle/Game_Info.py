import pygame
from settings import Settings

setting = Settings()

class Game_Info():
    def __init__(self,screen,size,font_color,
                 x,y):
        self.screen = screen
        self.font_size = size
        self.font_color = font_color
        self.font_x = x
        self.font_y = y
        self.font = pygame.font.SysFont(None,self.font_size)

    def draw_info(self,text):
        render_font = self.font.render(text,True,self.font_color)
        self.screen.blit(render_font,(self.font_x,self.font_y))



