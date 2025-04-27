# Розширені умовні конструкції в Python: if/elif/else

## Вкладені умовні конструкції (Nested if/else)
Іноді потрібно перевірити додаткові умови, коли початкова умова вже виконана:

- **Базовий синтаксис**:
  ```python
  if умова1:
      # код, який виконується, якщо умова1 істинна
      if умова2:
          # код, який виконується, якщо умова1 І умова2 істинні
      else:
          # код, який виконується, якщо умова1 істинна, але умова2 хибна
  else:
      # код, який виконується, якщо умова1 хибна
  ```

- **Приклад з перевіркою висоти та віку**:
  ```python
  height = int(input("Enter your height in cm: "))
  
  if height >= 120:
      print("You can ride the roller coaster.")
      age = int(input("What is your age? "))
      if age <= 18:
          print("Please pay $7.")
      else:
          print("Please pay $12.")
  else:
      print("Sorry, you have to grow taller before you can ride.")
  ```

## Конструкція if/elif/else
Коли є більше ніж два можливі шляхи виконання, використовуйте конструкцію if/elif/else:

- **Базовий синтаксис**:
  ```python
  if умова1:
      # код, який виконується, якщо умова1 істинна
  elif умова2:
      # код, який виконується, якщо умова1 хибна, але умова2 істинна
  elif умова3:
      # код, який виконується, якщо умова1 і умова2 хибні, але умова3 істинна
  else:
      # код, який виконується, якщо всі умови хибні
  ```

- **Приклад з різними ціновими категоріями за віком**:
  ```python
  height = int(input("Enter your height in cm: "))
  
  if height >= 120:
      print("You can ride the roller coaster.")
      age = int(input("What is your age? "))
      if age < 12:
          print("Please pay $5.")
      elif age <= 18:
          print("Please pay $7.")
      else:
          print("Please pay $12.")
  else:
      print("Sorry, you have to grow taller before you can ride.")
  ```

## Ключові особливості конструкції elif
- `elif` є скороченням від "else if"
- Можна використовувати скільки завгодно блоків `elif` між `if` та `else`
- Перевірка умов відбувається послідовно зверху вниз
- Виконується лише перший блок, умова якого істинна
- Блок `else` виконується тільки якщо жодна з попередніх умов не була істинною

## Додавання більшої кількості умов
```python
height = int(input("Enter your height in cm: "))

if height >= 120:
    print("You can ride the roller coaster.")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    elif age < 22:
        print("Please pay $9.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")
```

## Загальна схема прийняття рішень
1. Спочатку перевіряється основна умова (висота >= 120)
2. Якщо основна умова істинна, перевіряються додаткові умови (вік):
   - Якщо вік < 12: ціна $5
   - Інакше, якщо вік <= 18: ціна $7
   - Інакше (вік > 18): ціна $12
3. Якщо основна умова хибна, всі інші перевірки пропускаються

Конструкції `if/elif/else` дозволяють програмі обирати один з багатьох шляхів виконання залежно від різних умов, що робить ваш код більш гнучким та адаптивним.