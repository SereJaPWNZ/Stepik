# Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке) последовательными членами арифметической прогрессии.
# Формат входных данных
# На вход программе подаются три числа, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести «YES» или «NO» (без кавычек) в соответствии с условием задачи. 
# Тестовые данные 🟢
# Sample Input 1:
# 1
# 2
# 3
# Sample Output 1:
# YES
# Sample Input 2:
# 1
# 2
# 4

number1, number2, number3 = int(input()), int(input()), int(input())
if (number3 - number2) == (number2 -number1):
    print("YES")
else:
    print("NO")