import pygame
import sys
import random

cell_size = 30
grid_size = 20
screen_size = cell_size * grid_size
game_speed = 20

black = (0, 0, 0)
green = (0, 153, 0)
red = (255, 0, 0)
white = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode([screen_size, screen_size])
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

shake_x = [screen_size // 2]
shake_y = [screen_size // 2]
direction_x = cell_size
direction_y = 0


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


while True:
    screen.fill(black)
    for i in range(len(shake_x)):
        pygame.draw.rect(screen, green, [shake_x[i], shake_y[i], cell_size - 2, cell_size - 2])
        pygame.display.flip()
        clock.tick(60 / 20)
