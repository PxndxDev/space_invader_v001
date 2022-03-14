import pygame
import classes.nuclearMissile as nm

class NuclearEvent(pygame.sprite.Group):
    
    def __init__(self, window):
        super().__init__()
        self.charge = 0
        self.window = window

    def load(self, percent):
        self.charge += percent

    def launch_nuclear(self):
        self.charge = 0
        self.add(nm.NuclearMissile(self.window.player))