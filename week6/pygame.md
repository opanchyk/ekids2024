# Основні команди Pygame 
## на прикладі гри Snake 🐍

---

# 1. Ініціалізація Pygame

```python
# Імпорт та ініціалізація
import pygame
pygame.init()

# Створення вікна гри
screen_size = 600
screen = pygame.display.set_mode([screen_size, screen_size])
pygame.display.set_caption('Snake Game')

# Створення годинника для контролю FPS
clock = pygame.time.Clock()
```

**Пояснення:**
- `pygame.init()` - ініціалізує всі модулі Pygame
- `pygame.display.set_mode()` - створює вікно гри
- `pygame.display.set_caption()` - встановлює заголовок вікна
- `pygame.time.Clock()` - створює об'єкт для контролю частоти кадрів

---

# 2. Головний цикл гри

```python
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Оновлення екрану
    pygame.display.flip()
    clock.tick(60)  # 60 FPS
```

**Пояснення:**
- `pygame.event.get()` - отримує всі події (натискання клавіш, рух миші тощо)
- `pygame.display.flip()` - оновлює весь екран
- `clock.tick()` - контролює швидкість гри

---

# 3. Обробка подій клавіатури

```python
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT:
        direction_x = -cell_size
        direction_y = 0
    if event.key == pygame.K_RIGHT:
        direction_x = cell_size
        direction_y = 0
```

**Пояснення:**
- `pygame.KEYDOWN` - подія натискання клавіші
- `event.key` - код натиснутої клавіші
- `pygame.K_LEFT`, `pygame.K_RIGHT` і т.д. - константи для клавіш

---

# 4. Малювання на екрані

```python
# Заповнення екрану кольором
screen.fill(black)  # black = (0, 0, 0)

# Малювання прямокутника
pygame.draw.rect(screen, green, [x, y, width, height])

# Малювання тексту
font = pygame.font.Font(None, size)
text_surface = font.render("Game Over!", True, white)
screen.blit(text_surface, text_rect)
```

**Пояснення:**
- `screen.fill()` - заповнює екран кольором
- `pygame.draw.rect()` - малює прямокутник
- `font.render()` - створює поверхню з текстом
- `screen.blit()` - розміщує поверхню на екрані

---

# 5. Кольори та координати

```python
# Кольори в RGB форматі
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Система координат
# (0,0) - верхній лівий кут
# x збільшується вправо
# y збільшується вниз
```

**Пояснення:**
- Кольори задаються в RGB форматі (червоний, зелений, синій)
- Кожен компонент від 0 до 255
- Координати починаються з верхнього лівого кута

---

# 6. Колізії та зіткнення

```python
# Перевірка зіткнення зі стінами
if (x >= screen_size or x < 0 or 
    y >= screen_size or y < 0):
    game_over = True

# Перевірка зіткнення об'єктів
if snake_head.x == food.x and snake_head.y == food.y:
    score += 1
```

**Пояснення:**
- Колізії перевіряються порівнянням координат
- Можна перевіряти зіткнення з краями екрану
- Можна перевіряти перетин об'єктів

---

# 7. Рандомізація в Pygame

```python
import random

# Випадкова позиція для їжі
food_x = random.randrange(0, screen_size, cell_size)
food_y = random.randrange(0, screen_size, cell_size)
```

**Пояснення:**
- `random.randrange()` - генерує випадкове число в заданому діапазоні
- Третій параметр (cell_size) - крок між числами
- Використовується для розміщення об'єктів у випадкових місцях

---

# 8. Корисні поради

1. **FPS та швидкість гри**
   - Використовуйте `clock.tick()` для контролю швидкості
   - Не прив'язуйте логіку гри до FPS

2. **Структура коду**
   - Розділяйте логіку гри та відображення
   - Використовуйте функції для повторюваних дій

3. **Налагодження**
   - Використовуйте `print()` для відлагодження
   - Додайте відображення FPS та координат

---

# Корисні посилання

1. [Офіційна документація Pygame](https://www.pygame.org/docs/)
2. [Pygame Wiki](https://www.pygame.org/wiki/)
3. [Pygame туторіали](https://pygame.readthedocs.io/en/latest/index.html)
