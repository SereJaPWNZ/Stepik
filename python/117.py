# Наибольшие числа 🌶️🌶️

# На вход программе подается натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке. Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.
# Формат входных данных
# На вход программе подаются натуральное число n≥2, а затем n различных натуральных чисел, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести два наибольших числа, каждое на отдельной строке.

n, max_number, max_number_1 = int(input()), 1, 0
for i in range(n):
    temporary_number = int(input())
    if max_number < temporary_number:
        vrem = max_number
        max_number = temporary_number
        max_number_1 = vrem
    else:
        if max_number_1 < temporary_number:
            max_number_1 = temporary_number
print(max_number, max_number_1, sep='\n')