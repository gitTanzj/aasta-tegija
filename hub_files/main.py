import pygame
from level import Level
from player import Player

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
completed = ["Matemaatika", "Eesti keel", "Kehaline Kasvatus", "Progemine", "Terviseõpetus"]
ground1 = pygame.Rect(0, HEIGHT - 40, WIDTH, 40)
ground2 = pygame.Rect(0, HEIGHT // 2 - 40, WIDTH - 250, 40)
clock = pygame.time.Clock()

#NÄITAB SKOORI EKRAANIL
def draw_score():
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


# MÄNGU TSÜKKEL
def main():

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT or len(completed) == 0:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        the_player.run(keys_pressed, ground2)
        

        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()