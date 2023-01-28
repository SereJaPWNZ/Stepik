# max и min

# Дано натуральное число n,(n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры.
# Формат входных данных 
# На вход программе подается одно натуральное число.
# Формат выходных данных
# Программа должна вывести максимальную и минимальную цифры введенного числа (с поясняющей надписью).

n, max_number, min_number = int(input()), 0, 9
# var1
while n != 0:
    temp_number = n % 10
    if temp_number > max_number:
        max_number = temp_number
    if temp_number < min_number:
        min_number = temp_number
    n //= 10
print(f'Максимальная цифра равна {max_number}\nМинимальная цифра равна {min_number}')

# var 2
n = int(input())
print(f'Максимальная цифра равна {max(str(n))}\nМинимальная цифра равна {min(str(n))}')