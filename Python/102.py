# Даны два целых числа m и n (m ≤ n). Напишите программу, которая выводит все числа от m до n включительно.
# Формат входных данных
# На вход программе подаются два целых числа m и n, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести числа в соответствии с условием задачи.

m, n = int(input()), int(input())
for i in range(m, n+1):
    print(i)