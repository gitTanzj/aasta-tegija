import pygame
import os
import sqlite3 as sql

Skoor = 0
entry_1 = ""
pygame.init()
WIDTH, HEIGHT = 900, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Põgenege andmebaasi!")

conn = sql.connect('Vocostarter.db')
c = conn.cursor()

# Nuppud

# Font
Font = pygame.font.SysFont("comicsans", 40)

# Fotod
foto = pygame.image.load(os.path.join('progemine',"Viilu.png")).convert()
foto2 = pygame.image.load(os.path.join('progemine',"sqlite3.png")).convert()

# Värvid
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FPS = 60
run = True
clock = pygame.time.Clock()

# Kujundus
def kujundus():
    win.fill(BLACK)
    pygame.draw.rect(win, WHITE, pygame.Rect(150, 300, 500, 80))
    font_surface = Font.render(entry_1, True, BLACK)
    win.blit(font_surface, (160, 315))
    win.blit(foto, (100, 100))
    win.blit(foto2, (170, 150))
    pygame.display.update()

# Start
while run == True:
    clock.tick(FPS)
    kujundus()

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        # Text box
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                entry_1 = entry_1[:-1]
            elif event.key == pygame.K_RETURN:
                if entry_1 == "A" or entry_1 == "a":
                    # Punktid juurde
                    Skoor += 200
                    win.fill(WHITE)
                    text = Font.render("Olete võitnud!", 1, BLACK)
                    win.blit(text, (250, 180))
                    pygame.display.update()
                    pygame.time.delay(1000)
                    run = False
                else:
                    # Punktid maha
                    Skoor -= 200
                    win.fill(WHITE)
                    text = Font.render("Olete kaotanud!", 1, BLACK)
                    win.blit(text, (250, 180))
                    pygame.display.update()
                    pygame.time.delay(1000)
                    run = False
                entry_1 = ""
                c.execute(f'INSERT INTO Margus (SKOOR) VALUES ({Skoor})')
                conn.commit()
                conn.close()
            else:
                entry_1 += event.unicode

    pygame.display.flip()

pygame.quit()