# Даны пять чисел a_1, a_2, a_3, a_4, a_5. Напишите программу, которая вычисляет сумму их модулей |a_1| + |a_2| +|a_3| +|a_4| + |a_5|
# Формат входных данных
# На вход программе подается пять действительных чисел a_1, a_2, a_3, a_4, a_5, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести одно число – сумму модулей введённых чисел.

a1, a2, a3, a4, a5 = float(input()), float(input()), float(input()), float(input()), float(input())
sum_a = abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5)
print(sum_a)