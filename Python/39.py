# Напишите программу, которая определяет наименьшее из двух чисел.
# Формат входных данных
# На вход программе подаётся два различных целых числа.
# Формат выходных данных
# Программа должна вывести наименьшее из двух чисел.
# Sample Input 1:
# 8
# 11
# Sample Output 1:
# 8
# Sample Input 2:
# 20
# 5
# Sample Output 2:
# 5

number1, number2 = int(input()), int(input())
if number1 > number2:
    print(number2)
else:
    print(number1)