import pygame
import time
import classes.spaceship as sp
import classes.nuclearEvent as ne
import classes.missileEvent as ms
import classes.ovni as ov
import functions.collides as fct

class Window():

    def __init__(self, screen):
        self.gamemode = "Start screen"

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.background = pygame.image.load("./assets/backgrounds/0.jpg")
        self.background = pygame.transform.scale(self.background, (self.background.get_rect().width, self.screen_rect.height))

        self.player = sp.Spaceship(0, None, None, 4, self.screen)
        self.nuclearEvent = ne.NuclearEvent(self)
        self.missileEvent = ms.MissileEvent(self)
        self.allOvnis = pygame.sprite.Group()

        self.last_ovni = time.time()

    def update(self):
        # ajout de l'image de fond
        self.screen.blit(self.background, (0, 0))

        # affichage du joueur
        self.screen.blit(self.player.image, self.player.rect)

        # boucle des missiles sur le terrain
        for mis in self.missileEvent:
            mis.move()
            if mis.rect.y <= 0 - mis.rect.height:
                self.missileEvent.remove(mis)
            self.screen.blit(mis.image, mis.rect)

            if fct.collides(mis, self.allOvnis, False):
                self.missileEvent.remove(mis)

        # boucle des missiles nucléaires sur le terrain
        for nuke in self.nuclearEvent:
            nuke.move()
            if nuke.rect.y <= 0 - nuke.rect.height:
                self.nuclearEvent.remove(nuke)
            self.screen.blit(nuke.image, nuke.rect)

        # boucle des ovnis sur le terrain
        for ovni in self.allOvnis:
            if ovni.life <= 0:
                self.allOvnis.remove(ovni)
            else:
                if ovni.yLimit == ovni.rect.y:
                    ovni.shoot()
                else:
                    ovni.move()
                    
                    if ovni.rect.y >= self.screen.get_width():
                        self.allOvnis.remove(ovni)

                # boucle pour les missiles d'ovni
                for om in ovni.allMissiles:
                    om.move()

                    self.screen.blit(om.image, om.rect)

                # ----- COLLISIONS AVEC L'OVNI -----
                my_sprite = ovni
                my_bullet = Bullet(by, by)

                self.screen.blit(ovni.image, ovni.rect)

        # générateur d'ovnis
        if time.time() - self.last_ovni >= 4 and self.allOvnis.__len__() < 6:
            ovni = ov.Ovni()
            self.allOvnis.add(ovni)
            self.last_ovni = time.time()