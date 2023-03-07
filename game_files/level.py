import pygame
import os
from door import Door

# LEVELI KLASSI DEFINITSIOON
class Level():
    # ANNAB LEVELILE OMADUSED
    def __init__(self, surface):
        self.display_surface = surface

    # JOONISTAB MÄNGUMAASTIKU KOOS USTE JA PÕRANDATEGA EKRAANILE
    def setup_level(self,ground1, ground2, player):
        self.display_surface.fill((255,234,202))
        pygame.draw.rect(self.display_surface, (193,139,57), ground1)
        pygame.draw.rect(self.display_surface, (193,139,57), ground2)

        mata_uks = Door(self.display_surface, "Matemaatika")
        esta_uks = Door(self.display_surface, "Eesti keel")
        keka_uks = Door(self.display_surface, "Kehaline kasvatus")
        proge_uks = Door(self.display_surface, "Progemine")
        tervis_uks = Door(self.display_surface, "Terviseõpetus")

        proge_uks.run(20, ground2.y -150, player)
        mata_uks.run(200, ground2.y -150, player)
        esta_uks.run(380, ground2.y -150, player)
        tervis_uks.run(self.display_surface.get_width() - 170, ground1.y - 150, player)
        keka_uks.run(self.display_surface.get_width() - 370, ground1.y - 150, player)
