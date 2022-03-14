import pygame

class Missile(pygame.sprite.Sprite):

    def __init__(self, spaceship):
        super().__init__()

        self.spaceship = spaceship
        self.image = pygame.image.load("./assets/bullets/shoot.png")
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() / 5), int(self.image.get_height() / 5)))
        self.image = pygame.transform.rotate(self.image, -136)

        self.rect = self.image.get_rect()
        self.rect.y = self.spaceship.rect.y - self.spaceship.rect.height
        self.rect.x = self.spaceship.rect.x + (self.spaceship.rect.width / 2) - (self.image.get_width() / 2)

    def move(self):
        self.rect.y -= 10