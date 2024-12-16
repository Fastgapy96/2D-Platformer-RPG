import pygame
from settings import *
from background import *


class Level():

    def __init__(self):
        # Create the sky image
      self.background = Background


    def draw(self):
        # Draw sky image
        self.background.draw(self)

    def update(self):
        self.draw()
    