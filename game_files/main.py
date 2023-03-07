import pygame
from level import Level
from player import Player


pygame.init()
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('AASTA TEGIJA 2023')
level = Level(WIN)

SPEED = 5
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 100
FPS = 60
the_player = Player(WIN, PLAYER_HEIGHT, PLAYER_WIDTH)

ground2 = pygame.Rect(0, HEIGHT - 40, WIDTH, 40)
ground1 = pygame.Rect(0, HEIGHT//2 - 40, WIDTH - 250, 40)


def draw_window():
    level.run(ground1, ground2)
    the_player.draw_player()
    pygame.display.update()

def main():

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        the_player.run(keys=keys_pressed, grounds=[ground1,ground2])
        

        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()