import pygame
import time
import classes.window as wd

pygame.init()
pygame.display.set_allow_screensaver(True)

screen = pygame.display.set_mode((700, 700))
window = wd.Window(screen)

while True:
    time.sleep(0.01)
    if window.nuclearEvent.charge < 100:
        window.nuclearEvent.load(0.5)

    window.update()

    pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        window.player.move("left")
    if keys[pygame.K_z]:
        window.player.move("top")
    if keys[pygame.K_s]:
        window.player.move("bottom")
    if keys[pygame.K_d]:
        window.player.move("right")

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                if window.nuclearEvent.charge >= 100:
                    window.nuclearEvent.launch_nuclear()
            if event.button == 1:
                if window.missileEvent.__len__() <= 15:
                    window.missileEvent.launch_missile()