# Напишите программу, которая упорядочивает три числа от большего к меньшему.
# Формат входных данных
# На вход программе подается три целых числа, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести три числа, каждое на отдельной строке, упорядоченных от большего к меньшему.
int1, int2, int3 = int(input()), int(input()), int(input())
Min = min(int1, int2, int3)
Max = max(int1, int2, int3)
AVG = int1 + int2 + int3 - Max - Min
print(Max, AVG, Min, sep ='\n')