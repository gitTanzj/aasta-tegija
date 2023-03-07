import pygame
import os

# KARAKTERI KLASSI DEFINITSIOON
class Player:
    # ANNAB KARAKTERI KLASSILE OMADUSED
    def __init__(self, surface, height, width):
        self.rect_sprite = pygame.image.load(os.path.join("assets", "player2.png"))
        self.display_surface = surface
        self.speed = 5
        self.height = height
        self.width = width
        self.gravity = 5
        self.rect = pygame.Rect(10, 400, width, height)

    # JOONISTAB KARAKTERI EKRAANILE
    def draw_player(self):
        picture = pygame.transform.scale(self.rect_sprite, (self.width, self.height))
        self.display_surface.blit(picture, (self.rect.x, self.rect.y))
            
    # TEGELEB KARAKTERI LIIKUMISEGA
    def handle_player_movement(self, keys_pressed):
        if keys_pressed[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_d] and self.rect.x < self.display_surface.get_width():
            self.rect.x += self.speed
        if keys_pressed[pygame.K_w] and self.rect.bottom >= self.display_surface.get_height()-40:
            self.gravity -= 20
        
    # TEGELB KARAKTERI GRAVITATSIOONIGA
    def handle_player_gravity(self):
        self.gravity += 0.5
        self.rect.y += self.gravity
        if self.rect.bottom >= self.display_surface.get_height() - 40:
            self.rect.bottom = self.display_surface.get_height() - 40

    # TEGELEB KARAKTERI KOKKUPÕRKEGA TEISE KORRUSEGA
    def handle_floor_collision(self, ground2):
        if self.rect.colliderect(ground2) and self.rect.bottom >= ground2.top and self.rect.bottom <= ground2.bottom:
            self.rect.bottom = ground2.top
        if self.rect.colliderect(ground2) and self.rect.top <= ground2.bottom:
            self.gravity += 2
        
        
    # JOOKSUTAB KARAKTERI TEGEVUSI
    def run(self, keys, ground2):
        self.handle_player_movement(keys)
        self.handle_player_gravity()
        self.handle_floor_collision(ground2)
        

