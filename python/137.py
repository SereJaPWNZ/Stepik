# Ревью кода-2 🌶️🌶️

# На обработку поступает последовательность из 10 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают 10**6. Нужно написать программу, которая выводит на экран сумму всех отрицательных чисел последовательности и максимальное отрицательное число в последовательности. Если отрицательных чисел нет, требуется вывести на экран «NO». Программист торопился и написал программу неправильно.
# Найдите все ошибки в этой программе (их ровно 5). Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.
# Примечание 1. Число x не превышает по абсолютной величине 10**6, если −10**6<= x <= 10**6.
# Примечание 2. При необходимости вы можете добавить необходимые строки кода.

# origin
mx = 0
s = 0
for i in range(11):
    x = int(input())
    if x < 0:
        s = x
    if x > mx:
        mx = x
print(s)
print(mx)

# review

min = - 10 ** 6 - 1
s = 0
for i in range(10):
    x = int(input())
    if x < 0:
        s += x
    if x > min and x < 0:
        min = x
if s < 0:
    print(s, min, sep = '\n')
else:
    print('NO')
