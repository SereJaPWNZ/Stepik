# Дано трехзначное число abc, в котором все цифры различны. Напишите программу, которая выводит шесть чисел, образованных при перестановке цифр заданного числа.
# Формат входных данных
# На вход программе подаётся положительное трёхзначное целое число, все цифры которого различны.
# Формат выходных данных
# Программа должна вывести шесть чисел, образованных при перестановке цифр заданного числа в следующем порядке: abc, acb, bac, bca, cab, cba

number = int(input())
first = number // 100
second = number % 100 // 10
third = number % 10
print(number)
print(first, third, second, sep='')
print(second, first, third, sep='')
print(second, third, first, sep='')
print(third, first, second, sep='')
print(third, second, first, sep='')
