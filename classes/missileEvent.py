import pygame
import classes.missile as ms

class MissileEvent(pygame.sprite.Group):
    
    def __init__(self, window):
        super().__init__()
        self.window = window

    def launch_missile(self):
        self.add(ms.Missile(self.window.player))