# Напишите программу, которая принимает целое число x и определяет, принадлежит ли данное число указанным промежуткам.
# Формат входных данных
# На вход программе подаётся целое число x.
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

int1 = int(input())
if -30 < int1 <= -2 or 7 < int1 <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')