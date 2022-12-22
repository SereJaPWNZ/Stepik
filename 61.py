# Шахматная доска
# Заданы две клетки шахматной доски. Напишите программу, которая определяет имеют ли указанные клетки один цвет или нет. Если они покрашены в один цвет, то выведите слово «YES», а если в разные цвета — то «NO».
# Формат входных данных
# На вход программе подаётся четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# var1
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
dark = 0
light = 0
if x1 % 2 == 0:
    if y1 % 2 != 0:
        dark += 1
    else:
        light += 1
else:
    if y1 % 2 != 0:
        light += 1
    else:
        dark += 1
if x2 % 2 == 0:
    if y2 % 2 != 0:
        dark += 1
    else:
        light += 1
else:
    if y2 % 2 != 0:
        light += 1
    else:
        dark += 1
if dark == 2 or light == 2:
    print('YES')
else:
    print('NO')
    
#var 2    
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 + y1) % 2 == (x2 +y2) % 2:
    print('YES')
else:
    print('NO')