# Напишите программу, которая считывает целое число, после чего на экран выводится следующее и предыдущее целое число с пояснительным текстом.
# Формат входных данных
# На вход программе подаётся целое число.
# Формат выходных данных
# Программа должна вывести текст согласно условию задачи.
integer = int(input())
print(f'Следующее за числом {integer} число: {integer+1}\nДля числа {integer} предыдущее число: {integer-1}')
