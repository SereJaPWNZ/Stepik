# Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.
# Формат входных данных
# На вход программе подаётся положительное трёхзначное число.
# Формат выходных данных
# Программа должна вывести два числа с поясняющим текстом: сумма цифр и произведение цифр.

number = int(input())
The_last_number = number % 10
The_penultimate_number = number % 100 // 10
first_number = number // 100
print(f'Сумма цифр = {The_last_number+The_penultimate_number+first_number}\nПроизведение цифр = {The_last_number*The_penultimate_number*first_number}')