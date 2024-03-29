# Цифровой корень

# На вход программе подается натуральное число n. Напишите программу, которая находит цифровой корень данного числа. Цифровой корень числа n получается следующим образом: если сложить все цифры этого числа, затем все цифры найденной суммы и повторить этот процесс, то в результате будет получено однозначное число (цифра), которое и называется цифровым корнем данного числа.
# Формат входных данных
# На вход программе подается одно натуральное число.
# Формат выходных данных
# Программа должна вывести цифровой корень введенного числа.
# Примечание. Используйте вложенные циклы while.

n = int(input())
while n > 9:
    sum = 0
    while n > 0:
        last_digit = n % 10
        sum += last_digit
        n //= 10
    n = sum
print(n)    