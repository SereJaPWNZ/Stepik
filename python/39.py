# Напишите программу, которая определяет наименьшее из двух чисел.
# Формат входных данных
# На вход программе подаётся два различных целых числа.
# Формат выходных данных
# Программа должна вывести наименьшее из двух чисел.

num1, num2 = int(input()), int(input())
print(num1 if num1 < num2 else num2)