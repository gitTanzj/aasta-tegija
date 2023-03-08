import pygame
import os
from random import randint

class Obstacle:
    def __init__(self, display):
        self.display_surface = display
        self.sprite = pygame.image.load(os.path.join('assets', 'ob.png'))
        self.height = randint(50, 100)
        self.rect = pygame.Rect(display.get_width(), display.get_height() - 40 - self.height, 75, self.height)
        

    def draw_obstacle(self):
        obstacle = pygame.transform.scale(self.sprite, (self.rect.width, self.rect.height))
        self.display_surface.blit(obstacle, (self.rect.x, self.rect.y))
