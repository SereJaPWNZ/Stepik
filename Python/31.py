# Напишите программу, которая считывает два целых числа a и b и выводит на экран квадрат суммы (a+b)^2 и сумму квадратов a^2+b^2 этих чисел.
# Формат входных данных
# На вход программе подаётся два целых числа, каждое на отдельной строке.

number1 = int(input())
number2 = int(input())
print(f'Квадрат суммы {number1} и {number2} равен {(number1 + number2)**2}\nСумма квадратов {number1} и {number2} равна {number1**2 + number2**2}')