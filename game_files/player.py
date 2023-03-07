import pygame
import os

class Player:
    def __init__(self, surface, height, width):
        self.player_sprite = pygame.image.load(os.path.join("assets", "player2.png"))
        self.display_surface = surface
        self.speed = 5
        self.height = height
        self.width = width
        self.gravity = 5
        self.player = pygame.Rect(10, 400, width, height)

    def draw_player(self):
        picture = pygame.transform.scale(self.player_sprite, (self.width, self.height))
        self.display_surface.blit(picture, (self.player.x, self.player.y))
            

    def handle_player_movement(self, keys_pressed):
        if keys_pressed[pygame.K_a] and self.player.x > 0:
            self.player.x -= self.speed
        if keys_pressed[pygame.K_d] and self.player.x < self.display_surface.get_width():
            self.player.x += self.speed
        if keys_pressed[pygame.K_s] and self.player.y < self.display_surface.get_height() - 80:
            self.player.y += self.speed
        if keys_pressed[pygame.K_w] and self.player.bottom >= self.display_surface.get_height()-40:
            self.gravity -= 20
        
    def handle_player_gravity(self, grounds):
        self.gravity += 0.5
        self.player.y += self.gravity
        if self.player.bottom >= self.display_surface.get_height() - 40:
            self.player.bottom = self.display_surface.get_height() - 40
        

    def run(self, keys, grounds):
        self.handle_player_movement(keys)
        self.handle_player_gravity(grounds)
        

