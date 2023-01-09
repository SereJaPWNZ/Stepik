# Асимптотическое приближение

# На вход программе подается натуральное число n. Напишите программу, которая вычисляет значение выражения
# (1 + 1/2 + 1/3 + ... + 1/n) - ln(n)
# Примечание. Для вычисления натурального логарифма воспользуйтесь функцией log(n), которая находится в модуле math.

from math import log
sum_delit, n = 0, int(input())
for i in range(1, n + 1):
    delit = 1/i
    sum_delit += delit
total = sum_delit - log(n)
print(total)