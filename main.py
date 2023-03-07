import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
SPEED = 5
WHITE = (255,255,255)
FPS = 60
player_gravity = 0



def player_movement(keys_pressed, player):
    if keys_pressed[pygame.K_a] and player.x > 0:
        player.x -= SPEED
    if keys_pressed[pygame.K_d] and player.x < WIDTH:
        player.x += SPEED
    if keys_pressed[pygame.K_s] and player.y < HEIGHT - 80:
        player.y += SPEED
    if keys_pressed[pygame.K_w] and player.bottom >= HEIGHT-40:
        player.y -= SPEED
        global player_gravity
        player_gravity -= 20
 
    
    
    
def handle_player_gravity(player):
    global player_gravity
    player_gravity += 0.5
    player.y += player_gravity
    if player.bottom >= HEIGHT - 40:
        player.bottom = HEIGHT - 40

def draw_window(ground, player):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, (255,0,0), ground)
    pygame.draw.rect(WIN, (0,0,255), player)
    pygame.display.update()

def main():
    ground = pygame.Rect(0, HEIGHT - 40, WIDTH, 40)
    player = pygame.Rect(50, 400, 40, 40)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_w:
            #         if player.bottom >= HEIGHT-40:
            #             player.y -= SPEED
            #             global player_gravity
            #             player_gravity -= 20
        

        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed, player)
        handle_player_gravity(player)
        

        draw_window(ground, player)

    pygame.quit()


if __name__ == "__main__":
    main()