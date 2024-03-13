import os,re
import pygame

class Settings():
    def __init__(self):
        self.window_info()
        self.bg_info()
        self.blood_info()
        self.scores_info()
        self.time_info()
        self.hero_info()
        # self.enemy_hero_info()
        self.bullet_info()
        self.enemies_info()
        self.rock_info()
        self.recovery_info()
        self.explosion_info()
        self.music_volume_info()
        self.scores_file_info()
        self.start_info()
        self.over_info()
        self.pause_info()

    def window_info(self):
        self.window_width = 1000
        self.window_height = 600
        self.title = "Universe_battle"
        self.running = True
        self.game_fps = 80

    def bg_info(self):
        self.bg_path = "./images/bg1.png"
        self.bg_speed = 2

    def blood_info(self):
        self.health_bar_path = "./images/healthbar.png"
        self.blood_color = (9, 247, 9)
        self.blood_blocks = 10
        self.fix_health = 10


    def scores_info(self):
        self.scores = 0
        self.scores_size = 30
        self.scores_color = (255, 255, 255)

    def time_info(self):
        self.t_font_size = 30
        self.t_font_color = (255, 255, 255)
        self.event_space = 60
        self.hero_bullet_incr_time = 200
        self.hero_bullet_incr = 1


    def bullet_info(self):
        self.bullet_img_1_path = "./images/bullet1.png"
        self.bullet_img_2_path = "./images/bullet2.png"
        self.hero_bullet_speed = 8
        self.enemy_hero_bullet_speed = -8
        self.hero_bullet_limit = 3
        self.bullet1_img_load = pygame.image.load(self.bullet_img_1_path)
        self.bullet2_img_load = pygame.image.load(self.bullet_img_2_path)

        self.bullet1_img_width = self.bullet1_img_load.get_width()
        self.bullet1_img_height = self.bullet1_img_load.get_height()

        self.bullet2_img_width = self.bullet2_img_load.get_width()
        self.bullet2_img_height = self.bullet2_img_load.get_height()


    def hero_info(self):
        self.hero_img_path = "./images/hero_ship.png"
        self.hero_life = 10
        self.hero_size = (60,60)
        self.hero_speed_x = 5
        self.hero_speed_y = 5
        self.hero_img_load = pygame.image.load(self.hero_img_path)
        self.hero_img_width = self.hero_img_load.get_width()
        self.hero_img_height = self.hero_img_load.get_height()


    def enemies_info(self):
        self.alien_life = 1
        self.enemy_life= 2
        self.enemy_1_life = 1
        self.enemy_2_life = 3
        self.enemy_3_life = 8 # for it is hard to be killed
        self.hero_enemy_life = 10

        # self.alien_generation_space = 5
        # self.enemy_generation_space = 3
        # self.enemy_1_generation_space = 3
        # self.enemy_2_generation_space = 5
        # self.enemy_3_generation_space = 9
        # self.enemy_hero_generation_space = 13
        self.generation_space = 2.5


        self.alien_prob = 0.5
        self.enemy_prob = 0.5
        self.enemy_1_prob = 1
        self.enemy_2_prob = 0.5
        self.enemy_3_prob = 0.2
        self.enemy_hero_prob = 0.15

        self.enemy_hero_img_path = "./images/hero_enemy_ship.png"
        self.enemy_hero_speed = 1
        self.enemy_hero_img_load = pygame.image.load(self.enemy_hero_img_path)
        self.enemy_hero_img_width = self.enemy_hero_img_load.get_width()
        self.enemy_hero_img_height = self.enemy_hero_img_load.get_height()


        self.alien_img_path = "./images/alien.bmp"
        self.alien_speed = 5
        self.alien_img_load = pygame.image.load(self.alien_img_path)
        self.alien_img_width = self.alien_img_load.get_width()
        self.alien_img_height = self.alien_img_load.get_height()


        self.enemy_img_path = "./images/enemy.png"
        self.enemy_speed = 4
        self.enemy_img_load = pygame.image.load(self.alien_img_path)
        self.enemy_img_width = self.enemy_img_load.get_width()
        self.enemy_img_height = self.enemy_img_load.get_height()
        self.enemy_hero_fire_space = 1.3


        self.enemy_1_img_path = "./images/enemy1.png"
        self.enemy_1_speed = 2.5
        self.enemy_1_img_load = pygame.image.load(self.enemy_1_img_path)
        self.enemy_1_img_width = self.enemy_1_img_load.get_width()
        self.enemy_1_img_height = self.enemy_1_img_load.get_height()

        self.enemy_2_img_path = "./images/enemy2.png"
        self.enemy_2_speed = 2.5
        self.enemy_2_img_load = pygame.image.load(self.enemy_2_img_path)
        self.enemy_2_img_width = self.enemy_2_img_load.get_width()
        self.enemy_2_img_height = self.enemy_2_img_load.get_height()

        self.enemy_3_img_path = "./images/enemy3.png"
        self.enemy_3_speed = 1.2
        self.enemy_3_img_load = pygame.image.load(self.enemy_3_img_path)
        self.enemy_3_img_width = self.enemy_3_img_load.get_width()
        self.enemy_3_img_height = self.enemy_3_img_load.get_height()


    def rock_info(self):
        self.rock_big_imgs = ["./images/meteorBrown_big1.png","./images/meteorBrown_big2.png"]
        self.rock_small_imgs = ["./images/meteorBrown_med1.png","./images/meteorBrown_med3.png"]
        self.rock_big_prob = 0.2
        self.rock_small_prob = 0.3
        self.rock_generation_space = 5

        self.rock_big_img_1 = pygame.image.load(self.rock_big_imgs[0])
        self.rock_big_img_2 = pygame.image.load(self.rock_big_imgs[1])

        self.rock_big_img_1_width = self.rock_big_img_1.get_width()
        self.rock_big_img_1_height = self.rock_big_img_1.get_height()

        self.rock_big_img_2_width = self.rock_big_img_2.get_width()
        self.rock_big_img_2_height = self.rock_big_img_2.get_height()

        self.rock_small_img_1 = pygame.image.load(self.rock_small_imgs[0])
        self.rock_small_img_2 = pygame.image.load(self.rock_small_imgs[1])

        self.rock_small_img_1_width = self.rock_small_img_1.get_width()
        self.rock_small_img_1_height = self.rock_small_img_1.get_height()

        self.rock_small_img_2_width = self.rock_small_img_2.get_width()
        self.rock_small_img_2_height = self.rock_small_img_2.get_height()

    def recovery_info(self):
        self.recovery_generation_space = 10
        self.recovery_generation_prob = 0.1
        self.recovery_imgs = [
            "./images/bolt_gold.png","./images/shield_gold.png"
        ]
        self.recovery_1_img = pygame.image.load(self.recovery_imgs[0])
        self.recovery_2_img = pygame.image.load(self.recovery_imgs[0])

        self.recovery_1_img_width = self.recovery_1_img.get_width()
        self.recovery_1_img_height = self.recovery_1_img.get_height()

        self.recovery_2_img_width = self.recovery_2_img.get_width()
        self.recovery_2_img_height = self.recovery_2_img.get_height()

    def load_explosion_imgs(self):
        all_images = os.listdir("images")
        self.explosion_images = []
        for image in all_images:
            new_image = re.search(".*0\d\.png",image)
            if new_image:
                self.explosion_images.append(os.path.join(os.path.join(os.getcwd(),"images"),new_image.group()))

    def explosion_info(self):
        self.explosion_frame = 0.08
        self.load_explosion_imgs()

    def music_volume_info(self):
        self.main_music_1 = os.path.join(os.path.join(os.getcwd(),"audio"),"playing.ogg")
        self.main_music_2 = os.path.join(os.path.join(os.getcwd(),"audio"),"moonlight.wav")
        self.get_ready = os.path.join(os.path.join(os.getcwd(),"audio"),"getready.ogg")
        self.hero_shoot_volume = os.path.join(os.path.join(os.getcwd(),"audio"),"hero_shoot.wav")
        self.enemy_shoot_volume = os.path.join(os.path.join(os.getcwd(),"audio"),"enemy_shoot.mp3")
        self.bomb = os.path.join(os.path.join(os.getcwd(),"audio"),"bomb.ogg")
        self.fall = os.path.join(os.path.join(os.getcwd(),"audio"),"fall.mp3")
        self.rocket = os.path.join(os.path.join(os.getcwd(),"audio"),"rocket.ogg")
        self.start_music = os.path.join(os.path.join(os.getcwd(),"audio"),"start.wav")
        self.pause_moment = os.path.join(os.path.join(os.getcwd(),"audio"),"pause_moment.mp3")
        self.background_music = os.path.join(os.path.join(os.getcwd(),"audio"),"background_music.mp3")
        self.recovery_life = os.path.join(os.path.join(os.getcwd(),"audio"),"recovery_life.mp3")

    def scores_file_info(self):
        self.file_name = os.path.join(os.path.join(os.getcwd(),"high_scores.txt"))

    def start_info(self):
        self.start_img = os.path.join(os.path.join(os.getcwd(),"images"),"start_game_icon.png")

    def pause_info(self):
        self.pause_img = os.path.join(os.path.join(os.getcwd(),"images"),"game_pause_pressed.png")

    def over_info(self):
        self.over_img = os.path.join(os.path.join(os.getcwd(),"images"),"game_over.png")