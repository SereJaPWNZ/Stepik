# Обратное число

# Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему. Если при этом введённое с клавиатуры число – ноль, то вывести «Обратного числа не существует» (без кавычек).
# Формат входных данных 
# На вход программе подается одно действительное число.
# Формат выходных данных
# Программа должна вывести действительное число обратное данному, либо текст в соответствии с условием задачи.

number = float(input())
print('Обратного числа не существует' if number == 0 else number ** (-1))