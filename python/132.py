# Одинаковые цифры

# Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
# Формат входных данных 
# На вход программе подается одно натуральное число.
# Формат выходных данных
# Программа должна вывести «YES» если число состоит из одинаковых цифр и «NO» в противном случае.

# var1
n, flag = int(input()), True
text = 'YES'
while n > 9:
    last_n = n % 10
    first_n = n // 10 % 10
    if last_n == first_n:
        flag = True
    else:
        flag = False
        text = 'NO'
        n = 0
    n //= 10
print(text)

# var2
n = input()
max_n, min_n = max(n), min(n)
if max_n == min_n:
    print('YES')
else:
    print('NO')