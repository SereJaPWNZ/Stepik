# Напишите программу, вычисляющую объём куба и площадь его полной поверхности, по введённому значению длины ребра.
# Формат входных данных
# На вход программе подается одно целое число – длина ребра.
# Формат выходных данных
# Программа должна вывести текст и числа в соответствии с условием задачи.

The_length_of_the_rib = int(input())
print('Объем =', The_length_of_the_rib ** 3)
print('Площадь полной поверхности =', 6 * The_length_of_the_rib ** 2)