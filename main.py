import pygame
import sys
from settings import *
from level import Level

class Game():

#init
    pygame.init()

#window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('2DPlatformer')

level = Level()

running = True

#event handler
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    level.update()
    


pygame.quit()   
sys.exit         