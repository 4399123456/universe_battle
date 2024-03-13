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

        # bg1.draw()
        # bg1.move()

    def pause_handle(self,get_ready,start_time):
        # bg1.draw()
        # bg1.move()
        self.is_running = False
        self.screen.blit(self.pause_icon,(setting.window_width / 2 - self.pause_icon.get_width() / 2,
                                          setting.window_height / 2 - self.pause_icon.get_height() / 2))
        self.status_event(get_ready,start_time)


    def over_handle(self,get_ready,start_time):
        # bg1.draw()
        # bg1.move()
        self.is_running = False
        self.screen.blit(self.over_icon,(setting.window_width / 2 - self.over_icon.get_width() / 2,
                                         setting.window_height / 2 - self.over_icon.get_height() / 2))
        self.status_event(get_ready,start_time)

    def game_status(self,bg1,get_ready,start_music,background_music,
                    over_music,pause_music):
        # bg = Background(self.screen)
        start_time = time.time()
        is_enter = False

        # if self.is_start:
        #     start_music.action = "play"
        #     background_music.action = "stop"
        #     over_music.action = "stop"
        #     pause_music.action = "stop"
        #
        #     start_music.music_action()
        #     background_music.music_action()
        #     over_music.music_action()
        #     pause_music.music_action()

        # elif self.is_pause:
        #     pause_music.action = "play"
        #     background_music.action = "stop"
        #     over_music.action = "stop"
        #     start_music.action = "stop"
        #
        #     pause_music.music_action()
        #     background_music.music_action()
        #     over_music.music_action()
        #     start_music.music_action()

        # elif self.is_running:
        #     background_music.action = "play"
        #     start_music.action = "stop"
        #     pause_music.action = "stop"
        #     over_music.action = "stop"
        #
        #     background_music.music_action()
        #     start_music.music_action()
        #     pause_music.music_action()
        #     over_music.music_action()

        # elif self.is_over:
        #     over_music.action = "play"
        #     background_music.action = "stop"
        #     pause_music.action = "stop"
        #     start_music.action = "stop"
        #
        #     over_music.music_action()
        #     background_music.music_action()
        #     pause_music.music_action()
        #     start_music.music_action()

        while self.is_start or self.is_over or self.is_pause:
            is_enter = True
            # bg1.move()
            if self.is_start:
                self.start_handle(get_ready,start_time,bg1)
            elif self.is_over:
                self.over_handle(get_ready,start_time)
            elif self.is_pause:
                self.pause_handle(get_ready,start_time)
            pygame.display.update()
        return is_enter



