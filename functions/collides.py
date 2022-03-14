import pygame

def collides(spr, grp, doKill):
    return pygame.sprite.spritecollide(spr, grp, doKill)