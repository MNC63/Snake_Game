import pygame
from random import randint
from time import sleep

pygame.init()
screen = pygame.display.set_mode((601, 601))
pygame.display.set_caption('Snake')
running = True
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
clock = pygame.time.Clock()

snakes = [[9, 9], [9, 10], [9, 11]]
direction = "right"

apple = [randint(0, 19), randint(0, 19)]

while running:
    clock.tick(60)
    screen.fill(BLACK)

    tail_x = snakes[0][0]
    tail_y = snakes[0][1]

    # Draw grid
    for i in range(21):
        pygame.draw.line(screen, GREEN, (0, i * 30), (600, i * 30))
        pygame.draw.line(screen, GREEN, (i * 30, 0), (i * 30, 600))

    # Draw Apple
    pygame.draw.rect(screen, RED, (apple[0]*30, apple[1]*30, 30, 30))

    # Point
    if snakes[-1][0] == apple[0] and snakes[-1][1] == apple[1]:
        snakes.insert(0, [tail_x, tail_y])
        apple = [randint(0, 19), randint(0, 19)]

    # Draw snake
    for snake in snakes:
        pygame.draw.rect(screen, ORANGE, (snake[0]*30, snake[1]*30, 30, 30))

    if direction == "right":
        snakes.append([snakes[-1][0] + 1, snakes[-1][1]])
        snakes.pop(0)
    if direction == "left":
        snakes.append([snakes[-1][0] - 1, snakes[-1][1]])
        snakes.pop(0)
    if direction == "up":
        snakes.append([snakes[-1][0], snakes[-1][1] - 1])
        snakes.pop(0)
    if direction == "down":
        snakes.append([snakes[-1][0], snakes[-1][1] + 1])
        snakes.pop(0)

    sleep(0.1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP and direction != "down":
                direction = "up"
            if event.key == pygame.K_s or event.key == pygame.K_DOWN and direction != "up":
                direction = "down"
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
            if event.key == pygame.K_a or event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
    pygame.display.flip()

pygame.quit()
