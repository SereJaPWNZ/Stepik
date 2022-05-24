# Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение: сумма первой и последней цифр равна разности второй и третьей цифр.
# Формат входных данных
# На вход программе подаётся одно целое положительное четырёхзначное число.
# Формат выходных данных
# Программа должна вывести «ДА», если соотношение выполняется, и «НЕТ» — если не выполняется.
# Тестовые данные 🟢
# Sample Input 1:
# 1614
# Sample Output 1:
# ДА
# Sample Input 2:
# 1234
# Sample Output 2:
# НЕТ

number = int(input())
number1 = number // 1000
number2 = number % 1000 // 100
number3 = number % 100 // 10
number4 = number % 10

if (number1 + number4) == (number2 - number3):
    print("ДА")
else:
    print("НЕТ")