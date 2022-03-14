import pygame

class OvniMissile(pygame.sprite.Sprite):

    def __init__(self, ovni):
        super().__init__()

        self.ovni = ovni
        self.image = pygame.image.load("./assets/bullets/ovni_missile.png")
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() / 8), int(self.image.get_height() / 8)))
        self.image = pygame.transform.rotate(self.image, 45)

        self.rect = self.image.get_rect()
        self.rect.y = self.ovni.rect.y + self.ovni.rect.height
        self.rect.x = self.ovni.rect.x + (self.ovni.rect.width / 2) - (self.image.get_width() / 2)

        self.damages = 50

    def move(self):
        self.rect.y += 2