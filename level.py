import pygame
import os

class Level():
    def __init__(self, surface):
        self.display_surface = surface

    def setup_level(self):
        # taust
        self.display_surface.fill((255,234,202))
        # maastik
        pygame.draw.rect(self.display_surface, (193,139,57), pygame.Rect(0, self.display_surface.get_height() - 40, self.display_surface.get_width(), 40))
        


    def run(self):
        self.setup_level()
