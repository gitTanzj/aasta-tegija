import pygame
import os

pygame.init()
class Player:
    # ANNAB KARAKTERI KLASSILE OMADUSED
    def __init__(self, surface, height, width):
        self.rect_sprite = pygame.image.load(os.path.join("assets", "player2.png"))
        self.display_surface = surface
        self.speed = 5
        self.height = height
        self.width = width
        self.gravity = 5
        self.rect = pygame.Rect(150, 400, width, height)

    # JOONISTAB KARAKTERI EKRAANILE
    def draw_player(self):
        picture = pygame.transform.scale(self.rect_sprite, (self.width, self.height))
        self.display_surface.blit(picture, (self.rect.x, self.rect.y))
            
    # TEGELEB KARAKTERI LIIKUMISEGA
    def handle_player_movement(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w] and self.rect.bottom >= self.display_surface.get_height() - 40:
            self.gravity -= 25
        
    # TEGELB KARAKTERI GRAVITATSIOONIGA
    def handle_player_gravity(self):
        if self.gravity < 15:
            self.gravity += 0.5
            self.rect.y += self.gravity
        if self.rect.bottom >= self.display_surface.get_height() - 40:
            self.rect.bottom = self.display_surface.get_height() - 40
            
    # JOOKSUTAB KARAKTERI TEGEVUSI
    def run(self):
        self.handle_player_movement()
        self.handle_player_gravity()