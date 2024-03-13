import pygame

pygame.mixer.init()

class Game_Music():
    def __init__(self,name):
        self.music_name = name
        self.is_repeat = False
        self.action = "play"
        # create a threading to multi play music
        self.music_status = pygame.mixer.Sound(self.music_name)

    def music_action(self):
        if self.action == "play":
            if self.is_repeat:
                self.music_status.play(-1)
            else:
                self.music_status.play()

        if self.action == "pause":
            self.music_status.stop()
        if self.action == "stop":
            self.music_status.stop()


