# Напишите программу, которая определяет наименьшее из четырёх чисел.
# Формат входных данных
# На вход программе подаётся четыре целых числа.
# Формат выходных данных
# Программа должна вывести наименьшее из четырёх чисел.

a, b, c, d = int(input), int(input()), int(input()), int(input())
if a > b:
    ab = b
else:
    ab = a
if c > d:
    cd = d
else:
    cd = c
if ab > cd:
    print(cd)
else:
    print(ab)