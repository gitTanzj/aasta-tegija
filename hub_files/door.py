import pygame
import os
from subprocess import call

pygame.init()
class Door:
    def __init__(self, surface, subject, file):
        self.door_sprite = pygame.image.load(os.path.join("assets", "door_sprite.png"))
        self.subject = subject
        self.text = subject
        self.display_surface = surface
        self.file = file
        self.i = 0

    def draw_door(self, x, y):
        font = pygame.font.SysFont("comicsans", 18)
        text = font.render(self.text, 1, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (x + 50, y - 25)
        
        picture = pygame.transform.scale(self.door_sprite, (100, 150))
        self.display_surface.blit(picture, (x, y))
        self.display_surface.blit(text, textRect)

    def handle_file(self):
        # for ev in pygame.event.get():
        #     if ev.type == pygame.key:
        #         print('keydown')
        #         if ev.key == pygame.K_e:
        #             call(['python', self.file])
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e] and self.i <= 0:
            call(['python', self.file])
            self.i+=1
            

    def collide(self, player, x, y):
        doorRect = pygame.Rect(x, y, self.door_sprite.get_width(), self.door_sprite.get_height())
        if doorRect.colliderect(player):
            self.text = "Vajutage E nuppu"
            self.handle_file()
        else:
            self.text = self.subject


    def run(self, x, y, player):
        self.draw_door(x,y)
        self.collide(player, x, y)