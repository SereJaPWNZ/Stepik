# На вход программе подается натуральное число n. Напишите программу, которая вычисляет сумму всех его делителей.
# Входные данные
# На вход программе подается натуральное число n.
# Выходные данные
# Программа должна вывести единственное число в соответствии с условием задачи.
# Примечание. Функция подсчета суммы всех делителей числа является очень важной в теории чисел.

n = int(input())
sum_number = 0
for current_divider in range(1, n+1):
    if n % current_divider == 0:
        sum_number = current_divider + n // current_divider
print(sum_number)