# Входные данные
# На вход программе подаётся три целых числа: 
# b1, q и n, каждое на отдельной строке.
# Выходные данные
# Программа должна вывести 
# n
# n-ый член геометрической прогрессии.

b1, q, n = int(input()), int(input()), int(input())
print(b1 * q ** (n - 1))