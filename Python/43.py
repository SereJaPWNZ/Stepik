# Наишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.
# Формат входных данных
# На вход программе подаются три целых числа.
# Формат выходных данных
# Программа должна вывести одно число – сумму положительных чисел.
# Примечание. Если положительных чисел нет, то следует вывести 0.

int1, int2, int3 = int(input()), int(input()), int(input())
sum = 0
if int1 > 0:
    sum = sum + int1
if int2 > 0:
    sum = sum + int2
if int3 > 0:
    sum = sum + int3
print(sum)