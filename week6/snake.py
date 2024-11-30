import pygame
import random
import sys
import os

# Налаштування гри
cell_size = 30
grid_size = 20
screen_size = cell_size * grid_size
game_speed = 50

# Кольори (RGB)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)

# Налаштування pygame
pygame.init()
screen = pygame.display.set_mode([screen_size, screen_size])
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

# Початкові позиції змійки
snake_x = [screen_size // 2]
snake_y = [screen_size // 2]
direction_x = cell_size
direction_y = 0

# Створюємо першу їжу
food_x = round(random.randrange(0, screen_size - cell_size) / cell_size) * cell_size
food_y = round(random.randrange(0, screen_size - cell_size) / cell_size) * cell_size

score = 0
game_over = False

def show_text(text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Головний цикл гри
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction_x != cell_size:
                direction_x = -cell_size
                direction_y = 0
            if event.key == pygame.K_RIGHT and direction_x != -cell_size:
                direction_x = cell_size
                direction_y = 0
            if event.key == pygame.K_w and direction_y != cell_size:
                direction_y = -cell_size
                direction_x = 0
            if event.key == pygame.K_DOWN and direction_y != -cell_size:
                direction_y = cell_size
                direction_x = 0
            if event.key == pygame.K_SPACE and game_over:
                game_over = False
                snake_x = [screen_size // 2]
                snake_y = [screen_size // 2]
                direction_x = cell_size
                direction_y = 0
                score = 0

    if not game_over:
        new_head_x = snake_x[0] + direction_x
        new_head_y = snake_y[0] + direction_y

        if (new_head_x >= screen_size or new_head_x < 0 or
                new_head_y >= screen_size or new_head_y < 0):
            game_over = True

        for i in range(len(snake_x)):
            if new_head_x == snake_x[i] and new_head_y == snake_y[i]:
                game_over = True

        if not game_over:
            snake_x.insert(0, new_head_x)
            snake_y.insert(0, new_head_y)

            if new_head_x == food_x and new_head_y == food_y:
                os.system('say "beep"')  # для macOS
                # os.system('echo -e \\a')  # для Linux
                # os.system('echo \a')  # для Windows
                score += 1
                food_x = round(random.randrange(0, screen_size - cell_size) / cell_size) * cell_size
                food_y = round(random.randrange(0, screen_size - cell_size) / cell_size) * cell_size
                game_speed = game_speed - 5
            else:
                snake_x.pop()
                snake_y.pop()

    screen.fill(black)

    for i in range(len(snake_x)):
        pygame.draw.rect(screen, green, [snake_x[i], snake_y[i], cell_size - 2, cell_size - 2])

    pygame.draw.rect(screen, red, [food_x, food_y, cell_size - 2, cell_size - 2])

    show_text(f"Score: {score}", 35, 70, 20)

    if game_over:
        show_text("Game Over! Press SPACE to restart", 35, screen_size // 2, screen_size // 2)

    pygame.display.flip()
    clock.tick(60 / game_speed)
