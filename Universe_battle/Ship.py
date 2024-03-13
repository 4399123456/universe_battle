import pygame

'''
    Group for sprites store
'''

class Ship(pygame.sprite.Sprite):
    def __init__(self,screen,x,y,img_path,life,name):
        super().__init__()
        self.name = name
        self.screen = screen
        self.x = x
        self.y = y
        self.sprite_img = pygame.image.load(img_path)
        self.width = self.sprite_img.get_width()
        self.height = self.sprite_img.get_height()
        self.life = life
        self.setting_life = life
        self.rect = self.sprite_img.get_rect()


    def draw_sprite(self):
        self.screen.blit(self.sprite_img,(self.x,self.y))

    def move_sprite(self,speed_x,speed_y):
        self.x += speed_x
        self.y += speed_y


