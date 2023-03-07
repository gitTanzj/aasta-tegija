import pygame
import os
pygame.font.init()

class Door:
    def __init__(self, surface, text):
        self.door_sprite = pygame.image.load(os.path.join("assets", "door_sprite.png"))
        self.text = text
        self.display_surface = surface

    def draw_door(self, x, y):
        font = pygame.font.SysFont("comicsans", 18)
        text = font.render(self.text, 1, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (x + 50, y - 25)

        picture = pygame.transform.scale(self.door_sprite, (100, 150))
        self.display_surface.blit(picture, (x, y))
        self.display_surface.blit(text, textRect)

    def collide(self, player):
        doorRect = self.door_sprite.get_rect()
        if doorRect.colliderect(player):
            print("Touches door!")

    def run(self, x, y, player):
        self.draw_door(x,y)
        self.collide(player)