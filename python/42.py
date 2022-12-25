# Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.
# Формат входных данных
# На вход программе подаются три целых числа.
# Формат выходных данных
# Программа должна вывести одно число – сумму положительных чисел.
# Примечание. Если положительных чисел нет, то следует вывести
# 0.

# var1
number1, number2, number3 = int(input()), int(input()), int(input())
sum = 0
if number1 > 0:
    sum = sum + number1
if number2 > 0:
    sum = sum + number2
if number3 > 0:
    sum = sum + number3
print(sum)

# var2
number1, number2, number3 = int(input()), int(input()), int(input())
print(number1*(number1 > 0) + number2*(number2 > 0) + number3*(number3 > 0))