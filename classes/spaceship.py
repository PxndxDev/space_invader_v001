import pygame

class Spaceship(pygame.sprite.Sprite):

    def __init__(self, level, x, y, velocity, screen):
        super().__init__()

        self.velocity = velocity
        self.level = level
        if self.level == None or self.level < 0:
            self.level = 0
        if self.level > 6:
            self.level = 6
    
        self.image = pygame.image.load("./assets/spaceships/{}.png".format(self.level))
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()

        self.screen = screen

        if x == None:
            self.rect.x = (self.screen.get_rect().width / 2) - (self.rect.width / 2)
        else:
            self.rect.x = x

        if y == None:
            self.rect.y = self.screen.get_rect().height - self.rect.height
        else:
            self.rect.y = y

        self.maxLife = 200
        self.life = 200

    def move(self, direction):

        if direction == "left" and self.rect.x >= self.velocity:
            self.rect.x -= self.velocity

        elif direction == "right" and self.rect.x <= self.screen.get_width() - self.velocity - self.rect.width:
            self.rect.x += self.velocity

        elif direction == "top" and self.rect.y >= self.velocity:
            self.rect.y -= self.velocity
        
        elif direction == "bottom" and self.rect.y <= self.screen.get_height() - self.velocity - self.rect.height:
            self.rect.y += self.velocity