import pygame
import os

class Level():
    def __init__(self, surface):
        self.display_surface = surface

    def setup_level(self, ground1, ground2):
        # taust
        self.display_surface.fill((255,234,202))
        # maastik
        pygame.draw.rect(self.display_surface, (193,139,57), ground2)
        pygame.draw.rect(self.display_surface, (193,139,57), ground1)
        


    def run(self, ground1, ground2):
        self.setup_level(ground1, ground2)
