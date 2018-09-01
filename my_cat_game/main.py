import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('The CAT game')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'right'

while True: # the main game loop
    fpsClock.tick()
    DISPLAYSURF.fill(WHITE)

    for event in pygame.event.get():
        right_down = False

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_UP:
            pass
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            if catx >= 280:
                right_down = False
            else:
                right_down = True
        elif event.type == KEYDOWN and event.key == K_DOWN:
            if caty == 220:
                pass
            else:
                caty += 5
        elif event.type == KEYUP and event.key == K_RIGHT:
            right_down = False

    if right_down:
            if catx < 280:
                catx += 5

    DISPLAYSURF.blit(catImg, (catx, caty))
    pygame.display.update()
    fpsClock.tick(FPS)

    #print(fpsClock.get_fps())