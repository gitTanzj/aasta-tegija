import pygame
from random import randint

class Level:
    def __init__(self, surface):
        self.display_surface = surface

    def setup_level(self, ground):
        pygame.draw.rect(self.display_surface, (202,143,91), ground)


    def run(self, ground):
        self.setup_level(ground)
