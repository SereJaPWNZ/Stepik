# Формат входных данных
# На вход программе подается два вещественных числа aa и bb​, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.

a, b = float(input()), float(input())
Arithmetic_mean = (a + b)/2
Geometric_Mean = (a * b)**0.5
Average_Harmonic = 2*a*b/(a + b)
Mean_Square = ((a**2 + b**2)/2)**0.5
print(Arithmetic_mean, Geometric_Mean, Average_Harmonic, Mean_Square, sep = '\n')