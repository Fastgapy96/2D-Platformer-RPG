import pygame
from settings import *

class Background():
    
    def __init__(self,game):
        self.game = game
        self.screen = game.screen
        self.background=self.get_texture(r"resources\Background\background.png")

    def draw(self):
        # Draw sky image
        self.background

    @staticmethod
    def get_texture(SPRITESHEET_PATH, res=(SCREEN_WIDTH, SCREEN_HEIGHT)):
        texture = pygame.image.load(SPRITESHEET_PATH).convert_alpha()
        return pygame.transform.scale(texture, res)