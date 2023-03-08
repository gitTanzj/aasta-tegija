import pygame
import math
import sqlite3 as sql

conn = sql.connect("Vocostarter.db")
c = conn.cursor()

pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman!")

# Button
RADIUS = 20
GAP = 15
tähed = []
algus_x = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
algus_y = 400
A = 65
for i in range(26):
    x = algus_x + GAP * 2 + (RADIUS * 2 + GAP) * (i % 13)
    y = algus_y + ((i // 13) * (GAP + RADIUS * 2))
    tähed.append([x, y, chr(A + i), True])

# Font loomine
TÄHE_FONT = pygame.font.SysFont("comicsans", 35)
SÕNA_FONT = pygame.font.SysFont("comicsans", 55)

# Pildid
pildid = []
for i in range(7):
    pilt = pygame.image.load(r"hangman\assets\Hangman" + str(i) + ".png")
    pildid.append(pilt)
print(pildid)

# Game variables

hangman_olek = 0
sõna = "PROGRAMMEERIJA"
arvatud = []

# värvid
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
    win.fill(WHITE)
    
    # sõnad
    display_sõna = ""
    for täht in sõna:
        if täht in arvatud:
           display_sõna +=  täht + " "
        else:
            display_sõna += "_ "
    text = SÕNA_FONT.render(display_sõna, 1, BLACK)
    win.blit(text, (50, 20))

    # Buttons
    for täht in tähed:
        x, y, täh, nähtav = täht
        if nähtav:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = TÄHE_FONT.render(täh, 1, BLACK)
            win.blit(text, (x - text.get_width()/ 2, y - text.get_height()/ 2))

    win.blit(pildid[hangman_olek], (100, 150))
    pygame.display.update()

# Programmi algus paik
while run == True:
    clock.tick(FPS)

    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for täht in tähed:
                x, y, täh, nähtav = täht
                if nähtav:
                    distants = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if distants < RADIUS:
                    # [3] indexsis asub True statement
                        täht[3] = False
                        arvatud.append(täh)
                        if täh not in sõna:
                            hangman_olek += 1
    võitnud = True
    for täht in sõna:
        if täht not in arvatud:
            võitnud = False
            break
    if võitnud:
        pygame.time.delay(1000)
        win.fill("WHITE")
        text = SÕNA_FONT.render("Teie olete võitnud!", 1, BLACK)
        win.blit(text, (WIDTH/2 - text.get_width()/ 2, (HEIGHT / 2 - text.get_height()/ 2)))
        c.execute('INSERT INTO Eesti_keel (SKOOR) VALUES (100)')
        c.close()
        conn.commit()
        conn.close()
        pygame.display.update()
        pygame.time.delay(3000)
        break

    if hangman_olek == 6:
        pygame.time.delay(1000)
        win.fill("BLACK")
        text = SÕNA_FONT.render("Olete kaotanud!", 1, "WHITE")
        win.blit(text, (WIDTH/2 - text.get_width()/ 2, (HEIGHT / 2 - text.get_height()/ 2)))
        c.execute('INSERT INTO Eesti_keel (SKOOR) VALUES (-100)')
        c.close()
        conn.commit()
        conn.close()
        pygame.display.update()
        pygame.time.delay(3000)
        break

    

pygame.quit()