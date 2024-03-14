import random
import pygame

class Universe_Stuff(pygame.sprite.Sprite):
    def __init__(self,screen,x,y,image,attack,recovery_life,
                 speed_x,speed_y,name):
        super().__init__()
        self.name = name
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.image_2 = self.image.copy()
        self.rect = self.image.get_rect()
        self.attack = attack
        self.recovery_life = recovery_life
        self.rotate = 0
        self.rand_speed = random.randint(-3,3)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.last_update = pygame.time.get_ticks()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self):
        self.screen.blit(self.image,(self.x,self.y))

    def rotation(self):
        now_update = pygame.time.get_ticks()
        if now_update - self.last_update > 150:
            self.last_update = now_update
            self.rotate = (self.rotate + self.rand_speed) % 360
            self.rotate_img = pygame.transform.rotate(self.image,self.rotate)
            old_center = self.rect.center
            self.image = self.rotate_img
            self.rect = self.image.get_rect()
            self.rect.center = old_center


    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y








