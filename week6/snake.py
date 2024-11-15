import pygame
import random
import sys

# Налаштування гри
cell_size = 30  # Розмір однієї клітинки змійки
grid_size = 20  # Скільки клітинок буде по ширині і висоті
screen_size = cell_size * grid_size  # Загальний розмір вікна гри
game_speed = 20  # Швидкість гри (менше число = швидше)
# Спробуйте різні значення: 2 - дуже швидко, 10 - повільно

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

# Початкові позиції змійки (в центрі екрана)
snake_x = [screen_size // 2]  # Список для х-координат всіх частин змійки
snake_y = [screen_size // 2]  # Список для у-координат всіх частин змійки
direction_x = cell_size  # Напрямок руху по х
direction_y = 0  # Напрямок руху по у

# Створюємо першу їжу в випадковому місці
food_x = round(random.randrange(0, screen_size - cell_size) / cell_size) * cell_size
food_y = round(random.randrange(0, screen_size - cell_size) / cell_size) * cell_size

score = 0
game_over = False


# Функція для показу тексту на екрані
def show_text(text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)


# Головний цикл гри
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Якщо натиснули на хрестик - закриваємо гру
            pygame.quit()
            sys.exit()

        # Керування змійкою
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction_x != cell_size:
                direction_x = -cell_size
                direction_y = 0
            if event.key == pygame.K_RIGHT and direction_x != -cell_size:
                direction_x = cell_size
                direction_y = 0
            if event.key == pygame.K_UP and direction_y != cell_size:
                direction_y = -cell_size
                direction_x = 0
            if event.key == pygame.K_DOWN and direction_y != -cell_size:
                direction_y = cell_size
                direction_x = 0
            # Перезапуск гри після програшу
            if event.key == pygame.K_SPACE and game_over:
                game_over = False
                snake_x = [screen_size // 2]
                snake_y = [screen_size // 2]
                direction_x = cell_size
                direction_y = 0
                score = 0

    if not game_over:
        # Рух змійки
        new_head_x = snake_x[0] + direction_x
        new_head_y = snake_y[0] + direction_y

        # Перевірка зіткнення зі стінами
        if (new_head_x >= screen_size or new_head_x < 0 or
                new_head_y >= screen_size or new_head_y < 0):
            game_over = True

        # Перевірка зіткнення з тілом змійки
        for i in range(len(snake_x)):
            if new_head_x == snake_x[i] and new_head_y == snake_y[i]:
                game_over = True

        if not game_over:
            # Додаємо нову позицію голови
            snake_x.insert(0, new_head_x)
            snake_y.insert(0, new_head_y)

            # Перевірка чи з'їли їжу
            if new_head_x == food_x and new_head_y == food_y:
                score += 1
                # Створюємо нову їжу
                food_x = round(random.randrange(0, screen_size - cell_size) / cell_size) * cell_size
                food_y = round(random.randrange(0, screen_size - cell_size) / cell_size) * cell_size
            else:
                # Якщо не з'їли їжу - видаляємо останній елемент змійки
                snake_x.pop()
                snake_y.pop()

    # Малюємо все на екрані
    screen.fill(black)  # Чорний фон

    # Малюємо змійку
    for i in range(len(snake_x)):
        pygame.draw.rect(screen, green, [snake_x[i], snake_y[i], cell_size - 2, cell_size - 2])

    # Малюємо їжу
    pygame.draw.rect(screen, red, [food_x, food_y, cell_size - 2, cell_size - 2])

    # Показуємо рахунок
    show_text(f"Score: {score}", 35, 70, 20)

    # Якщо гра закінчена - показуємо повідомлення
    if game_over:
        show_text("Game Over! Press SPACE to restart", 35, screen_size // 2, screen_size // 2)

    # Оновлюємо екран
    pygame.display.flip()

    # Встановлюємо швидкість гри
    clock.tick(60 / game_speed)  # Формула для перетворення game_speed у кадри в секунду
