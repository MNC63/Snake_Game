import pygame

pygame.init()
screen = pygame.display.set_mode((601, 601))
pygame.display.set_caption('Snake')
running = True
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
clock = pygame.time.Clock()

snake = [9, 9]


while running:
    clock.tick(60)
    screen.fill(BLACK)

    # Draw grid
    for i in range(21):
        pygame.draw.line(screen, GREEN, (0, i * 30), (600, i * 30))
        pygame.draw.line(screen, GREEN, (i * 30, 0), (i * 30, 600))

    # Draw snake
    pygame.draw.rect(screen, WHITE, (snake[0]*30, snake[1]*30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
