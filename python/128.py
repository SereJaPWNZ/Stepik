# Обратный порядок 2

# Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.
# Формат входных данных 
# На вход программе подается одно натуральное число.
# Формат выходных данных
# Программа должна вывести число, записанное в обратном порядке.

number = int(input())
while number != 0:
    Reverse_number = number % 10
    print(Reverse_number, end='')
    number //= 10