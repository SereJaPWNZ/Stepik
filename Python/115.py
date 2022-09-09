# Напишите программу, которая считывает последовательность из 10 целых чисел и определяет является ли каждое из них четным или нет.
# Формат входных данных
# На вход программе подаются 10 целых чисел, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести строку «YES», если все числа четные и «NO» в ином случае.

count = 1
for i in range(1, 11):
    vrem = int(input())
    if vrem % 2 == 0:
        count = count + 1
if count == 11:
    print('YES')
else:
    print('NO')