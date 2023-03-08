import pygame
from level import Level
from player import Player
from obstacle import Obstacle
import os
from random import randint


pygame.init()
WIDTH, HEIGHT = 900, 500
PLAYER_WIDTH, PLAYER_HEIGHT = 100, 150
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Kehaline kasvatus')
FPS = 60
SPEED = randint(5, 10)
SCORE = 330

level = Level(WIN)
ground = pygame.Rect(0, HEIGHT - 40, WIDTH, 40)
player = Player(WIN, PLAYER_HEIGHT, PLAYER_WIDTH)
obstacles = [Obstacle(WIN) for _ in range(15)]

def show_score():
    font = pygame.font.SysFont("comicsans", 18)
    text = font.render(f"SKOOR : {SCORE}", 1, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, 75)
    WIN.blit(text, textRect)

def draw_window():
    WIN.blit(pygame.image.load(os.path.join('assets', 'kehka_bg.png')), (0,0))
    show_score()
    level.run(ground)
    player.draw_player()
    for i in obstacles:
        i.draw_obstacle()
    pygame.display.update()

def main():

    global SCORE
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                run = False

        if len(obstacles) != 0:
            if obstacles[0].rect.colliderect(player.rect):
                SCORE -= 1
            if obstacles[0].rect.x <= 0:
                obstacles.pop(0)
            else:
                obstacles[0].rect.x -= SPEED
        
        
        player.run()

        draw_window()
    pygame.quit()



if __name__ == "__main__":
    main()