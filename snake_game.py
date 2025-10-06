import pygame
from random import randint

pygame.init()


WIDTH, HEIGHT = 600, 600
CELL_SIZE = 30
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake 🐍")
clock = pygame.time.Clock()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


font_small = pygame.font.SysFont("Arial", 20)
font_big = pygame.font.SysFont("Arial", 40)

snakes = [[5, 10], [6, 10], [7, 10]]
direction = "right"
score = 0
speed = 10
time_counter = 0
running = True
pausing = False


def spawn_apple():
    while True:
        x = randint(0, COLS - 1)
        y = randint(0, ROWS - 1)
        if [x, y] not in snakes:
            return [x, y]


def load_best_score():
    try:
        with open("best_score.txt", "r") as f:
            return int(f.read())
    except:
        return 0


def save_best_score(score):
    with open("best_score.txt", "w") as f:
        f.write(str(score))


best_score = load_best_score()
apple = spawn_apple()


def draw_grid():
    for i in range(ROWS):
        pygame.draw.line(screen, WHITE, (0, i*30), (HEIGHT, i*30))
        pygame.draw.line(screen, WHITE, (i*30, 0), (i*30, WIDTH))


def draw_snake():
    for x, y in snakes:
        pygame.draw.rect(screen, GREEN, (x * CELL_SIZE, y * CELL_SIZE,
                                         CELL_SIZE, CELL_SIZE))


def draw_apple():
    pygame.draw.rect(
        screen, RED, (apple[0]*CELL_SIZE, apple[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))


def draw_score():
    text = font_small.render(f"Scores: {score}", True, WHITE)
    best_text = font_small.render(f"Best: {best_score}", True, WHITE)
    screen.blit(text, (5, 5))
    screen.blit(best_text, (5, 30))


while running:
    screen.fill(BLACK)
    clock.tick(speed)  # control speed
    time_counter += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if (event.key in (pygame.K_UP, pygame.K_w)) and direction != "down":
                direction = "up"
            elif (event.key in (pygame.K_DOWN, pygame.K_s)) and direction != "up":
                direction = "down"
            elif (event.key in (pygame.K_RIGHT, pygame.K_d)) and direction != "left":
                direction = "right"
            elif (event.key in (pygame.K_LEFT, pygame.K_a)) and direction != "right":
                direction = "left"
            elif event.key == pygame.K_SPACE and pausing:
                snakes = [[5, 10], [6, 10], [7, 10]]
                direction = "right"
                apple = spawn_apple()
                score = 0
                pausing = False

    # Game Logic
    if not pausing:
        head_x, head_y = snakes[-1]

        if direction == "up":
            head_y -= 1
        if direction == "down":
            head_y += 1
        if direction == "right":
            head_x += 1
        if direction == "left":
            head_x -= 1

        new_head = [head_x, head_y]

        # check collision
        if (
            head_x < 0 or head_x >= COLS or
            head_y < 0 or head_y >= ROWS
            or new_head in snakes
        ):
            pausing = True
        else:
            snakes.append(new_head)
            if score > best_score:
                best_score = score
                save_best_score(best_score)

            # Get Point
            if new_head == apple:
                score += 1
                apple = spawn_apple()
                speed = 10 + score // 3  # up 1 speed every 3 point
            else:
                snakes.pop()
        if time_counter % 1000 == 0:
            speed += 1

    # Drawing
    draw_snake()
    draw_apple()
    draw_score()

    # Game over screen
    if pausing:
        pygame.draw.rect(screen, BLACK, (0, HEIGHT // 2 - 60, WIDTH, 120))
        game_over_txt = font_big.render(
            f"Game Over! Scores: {score}", True, WHITE)
        press_space_txt = font_big.render(
            f"Press SPACE to restart", True, WHITE)
        screen.blit(game_over_txt, (WIDTH // 2 -
                    game_over_txt.get_width() // 2, HEIGHT // 2 - 30))
        screen.blit(press_space_txt, (WIDTH // 2 -
                    press_space_txt.get_width() // 2, HEIGHT // 2 + 20))

    pygame.display.flip()

pygame.quit()
