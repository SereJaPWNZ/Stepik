# Численный треугольник 1

# Дано натуральное число n. Напишите программу, которая печатает численный треугольник в соответствии с примером:
# 1
# 22
# 333
# 4444
# 55555
# ...
# Формат входных данных
# На вход программе подается одно натуральное число.
# Формат выходных данных
# Программа должна вывести треугольник в соответствии с условием.
# Примечание. Используйте вложенный цикл for.

# var 1
number, counter = int(input()), 1
for i in range(1, number + 1):
    print(counter*f'{i}')
    counter += 1

# var 2
number = int(input())
for i in range(1, number  + 1):
    for _ in range(i, i + 1):
        print(str(_) * i)
