# Напишите программу, вычисляющую значение тригонометрического выражения по заданному числу градусов x.
# Формат входных данных
# На вход программе подается одно вещественное число x измеряемое в градусах​. 
# Формат выходных данных
# Программа должна вывести одно число – значение тригонометрического выражения.

from math import *
int = float(input())
rad = int * pi / 180
trigonometric_expression = sin(rad) + cos(rad) + tan(rad)*tan(rad)
print(trigonometric_expression)