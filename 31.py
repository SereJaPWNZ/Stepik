# Напишите программу, которая считывает два целых числа
# a и b и выводит на экран квадрат суммы и сумму квадратов этих чисел.
# Формат входных данных
# На вход программе подаётся два целых числа, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием.

a, b = int(input()), int(input())
print(f'Квадрат суммы {a} и {b} равен {(a+b)**2}\nСумма квадратов {a} и {b} равна {a**2+b**2}')