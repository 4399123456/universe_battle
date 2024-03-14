import pygame
import sys,time
from settings import Settings
from Background import Background



setting = Settings()
class Game_Status():
    def __init__(self,screen):
        self.screen = screen
        self.is_start = True
        self.is_running = False
        self.is_over = False
        self.is_pause = False
        self.start_icon = pygame.image.load(setting.start_img)
        self.pause_icon = pygame.image.load(setting.pause_img)
        self.over_icon = pygame.image.load(setting.over_img)


    def status_event(self,get_ready,start_time):

        end_time = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.is_start:
                    get_ready.music_action()
                if self.is_start:
                    self.is_start = False
                    self.is_running = True
                    self.is_over = False
                    self.is_pause = False
                elif self.is_over:
                    self.is_over = False
                    self.is_running = True
                    self.is_start = False
                    self.is_pause = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.is_start:
                        get_ready.music_action()
                    if self.is_start:
                        self.is_start = False
                        self.is_running = True
                        self.is_over = False
                        self.is_pause = False
                    elif self.is_over:
                        self.is_over = False
                        self.is_running = True
                        self.is_over = False
                        self.is_pause = False

                elif event.key == pygame.K_ESCAPE:
                    self.is_pause = False
                    self.is_running = True
                    self.is_over = False
                    self.is_start = False

    def start_handle(self,get_ready,start_time,bg1):

        bg1.draw()
        self.is_running = False
        self.screen.blit(self.start_icon, (setting.window_width / 2 - self.start_icon.get_width() / 2,
                                           setting.window_height / 2 - self.start_icon.get_height() / 2))
        self.status_event(get_ready,start_time)

    def pause_handle(self,get_ready,start_time):
        self.is_running = False
        self.screen.blit(self.pause_icon,(setting.window_width / 2 - self.pause_icon.get_width() / 2,
                                          setting.window_height / 2 - self.pause_icon.get_height() / 2))
        self.status_event(get_ready,start_time)

    def over_handle(self,get_ready,start_time):
        self.is_running = False
        self.screen.blit(self.over_icon,(setting.window_width / 2 - self.over_icon.get_width() / 2,
                                         setting.window_height / 2 - self.over_icon.get_height() / 2))
        self.status_event(get_ready,start_time)

    def game_status(self,bg1,get_ready,start_music,background_music,
                    over_music,pause_music):
        start_time = time.time()
        is_enter = False

        while self.is_start or self.is_over or self.is_pause:
            is_enter = True
            if self.is_start:
                self.start_handle(get_ready,start_time,bg1)
            elif self.is_over:
                self.over_handle(get_ready,start_time)
            elif self.is_pause:
                self.pause_handle(get_ready,start_time)
            pygame.display.update()
        return is_enter



