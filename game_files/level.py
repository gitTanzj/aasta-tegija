import pygame
from door import Door
import os


pygame.init()
# LEVELI KLASSI DEFINITSIOON
class Level():
    # ANNAB LEVELILE OMADUSED
    def __init__(self, surface):
        self.display_surface = surface
        self.mata_uks = Door(self.display_surface, "Matemaatika", os.path.join('Erki_Ül', 'Erki_ülesanne.py'))
        self.esta_uks = Door(self.display_surface, "Eesti keel", os.path.join('hangman', 'main.py'))
        self.keka_uks = Door(self.display_surface, "Kehaline kasvatus", os.path.join('keka', 'main.py'))
        self.proge_uks = Door(self.display_surface, 'Progemine', 'margus.py')
        self.tervis_uks = Door(self.display_surface, "Terviseõpetus", os.path.join('Riina_ülesanne', 'bioloogia_viktoriin.py'))

    # JOONISTAB MÄNGUMAASTIKU KOOS USTE JA PÕRANDATEGA EKRAANILE
    def setup_level(self,ground1, ground2, player):
        self.display_surface.fill((255,234,202))
        pygame.draw.rect(self.display_surface, (193,139,57), ground1)
        pygame.draw.rect(self.display_surface, (193,139,57), ground2)

        
        self.mata_uks.run(200, ground2.y - 150, player)
        self.esta_uks.run(380, ground2.y - 150, player)
        self.tervis_uks.run(self.display_surface.get_width() - 170, ground1.y - 150, player)
        self.keka_uks.run(self.display_surface.get_width() - 370, ground1.y - 150, player)
        self.proge_uks.run(20, ground2.y - 150, player)
