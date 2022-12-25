# Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение: сумма первой и последней цифр равна разности второй и третьей цифр.
# Формат входных данных
# На вход программе подаётся одно целое положительное четырёхзначное число.
# Формат выходных данных
# Программа должна вывести «ДА», если соотношение выполняется, и «НЕТ» — если не выполняется.


# variant 1
number = int(input())
first_number = number // 1000
second_number = number % 1000 // 100
third_number = number % 100 // 10
fourth_number = number % 10
if (first_number+fourth_number) == (second_number - third_number):
    print('ДА')
else:
    print('НЕТ')
    
# variant 2
a, b, c, d = input()
if int(a) + int(d) == int(b) - int(c):
    print('ДА')
else:
    print('НЕТ')