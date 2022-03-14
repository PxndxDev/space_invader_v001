import pygame
import random
import time
import classes.ovniMissile as om

class Ovni(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.velocity = 1
    
        self.image = pygame.image.load("./assets/entities/ovni.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        self.rect.y = -random.randint(0, 100)
        self.rect.x = random.randint(0, 700 - self.rect.width)
        self.yLimit = random.randint(50, 110)

        self.allMissiles = pygame.sprite.Group()
        self.lastMissile = time.time()

        self.maxLife = 50;
        self.life = 50;

    def move(self):
        self.rect.y += self.velocity

    def shoot(self):
        if time.time() - self.lastMissile >= 2.5:
            self.lastMissile = time.time()
            newMissile = om.OvniMissile(self)
            self.allMissiles.add(newMissile)