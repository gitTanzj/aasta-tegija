import pygame
from level import Level
from player import Player
import sqlite3 as sql
from database import databaseInit
import os

pygame.init()

# MÄNGUKS VAJALIKUD MUUTUJAD
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('VOCO-STARTER')
level = Level(WIN)
SCORE = 0
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 75
FPS = 60
the_player = Player(WIN, PLAYER_HEIGHT, PLAYER_WIDTH)
ained = ["Riina", "Kehaline", "Erki", "Eesti_keel", "Margus"]
ground1 = pygame.Rect(0, HEIGHT - 40, WIDTH, 40)
ground2 = pygame.Rect(0, HEIGHT // 2 - 40, WIDTH - 250, 40)
clock = pygame.time.Clock()

if not os.path.exists('Vocostarter.db'):
    databaseInit(ained)

conn = sql.connect("Vocostarter.db")
c = conn.cursor()

#NÄITAB SKOORI EKRAANIL
def draw_score():

    c.execute("SELECT sum(SKOOR) FROM Riina")
    table1_scores = c.fetchall()
    c.execute("SELECT sum(SKOOR) FROM Kehaline")
    table2_scores = c.fetchall()
    c.execute("SELECT sum(SKOOR) FROM Erki")
    table3_scores = c.fetchall()
    c.execute("SELECT sum(SKOOR) FROM Eesti_keel")
    table4_scores = c.fetchall()
    c.execute("SELECT sum(SKOOR) FROM Margus")
    table5_scores = c.fetchall()
    

    def add_scores(*args):
        res = 0
        for i in args:
            if i == None:
                i = 0
            res += i
        return res
    
    SCORE = add_scores(table1_scores[0][0], table2_scores[0][0], table3_scores[0][0], table4_scores[0][0], table5_scores[0][0])

    font = pygame.font.SysFont("comicsans", 18)
    text = font.render(f"Skoor : {SCORE}", 1, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (WIDTH - 150, 75)
    WIN.blit(text, textRect)
# JOONISTAB EKRAANI
def draw_window():
    level.setup_level(ground1, ground2, the_player.rect)
    the_player.draw_player()
    draw_score()
    pygame.display.update()

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x - textrect.width // 2, y)
    surface.blit(textobj, textrect)


click = False
# MÄNGU TSÜKKEL
def main():
    
    def game():
        run = True
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():

                if event.type == pygame.QUIT or len(ained) == 0:
                    run = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pass
            
            keys_pressed = pygame.key.get_pressed()
            the_player.run(keys_pressed, ground2)
            

            draw_window()
        for i in ained:
            print(f'deleting from {i}')
            c.execute(f"DELETE FROM {i}")
        conn.commit()
        conn.close()
        pygame.quit()
    
    def credits():
        pass

    while True:
        mainFont = pygame.font.SysFont("comicsans", 64)
        buttonFont = pygame.font.SysFont('comicsans', 28)
        WIN.fill((112,112,112))
        draw_text('VOCOSTARTER', mainFont, (255,255,255), WIN, WIDTH // 2, HEIGHT * 0.2)
        
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(WIDTH // 2 - 100, HEIGHT * 0.5, 200, 50)
        button_2 = pygame.Rect(WIDTH // 2 - 100, HEIGHT * 0.7, 200, 50)

        if button_1.collidepoint((mx,my)):
            if click:
                game()
        elif button_2.collidepoint((mx,my)):
            if click:
                credits()
        pygame.draw.rect(WIN, (183,183,183), button_1)
        pygame.draw.rect(WIN, (183,183,183), button_2)

        draw_text('Mängi', buttonFont, (255,255,255), WIN, WIDTH // 2, HEIGHT * 0.5)
        draw_text('Credits', buttonFont, (255,255,255), WIN, WIDTH // 2, HEIGHT * 0.7)

        
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(FPS)
    


if __name__ == "__main__": 
    main()
