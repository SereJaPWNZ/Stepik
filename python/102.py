# Популяция

# На вход программе подается три натуральных числа m,p,n:
# m: стартовое количество организмов;
# p: среднесуточное увеличение в %;
# n: количество дней для размножения.
# Напишите программу, которая предсказывает размер популяции организмов. Программа должна выводить размер популяции в каждый день, начиная с 1 и заканчивая n-м днем.
# Формат входных данных
# На вход программе подается три натуральных числа.
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

m, p, n = int(input()), int(input()), int(input())
for i in range(1, n + 1):
    print(i, m)
    m = m + m * (p / 100)