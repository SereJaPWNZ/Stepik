# Ревью кода-1 🌶️🌶️

# На обработку поступает последовательность из 10 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают 10**6. Нужно написать программу, которая выводит на экран количество неотрицательных чисел последовательности и их произведение. Если неотрицательных чисел нет, требуется вывести на экран «NO». Программист торопился и написал программу неправильно.
# Найдите все ошибки в этой программе (их ровно 4). Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.
# Примечание 1. Число x не превышает по абсолютной величине 10**6, если −10**6<= x <= 10**6
# Примечание 2. При необходимости вы можете добавить необходимые строки кода.

# origin

count = 0
p = 0
for i in range(1, 10):
    x = int(input())
    if x > 0:
        p = p * x
        count = count + 1
if count > 0:
    print(x)
    print(p)
else:
    print('NO')
    
# review

total_positive_numbers = 0
work_of_numbers = 1
for i in range(1, 11):
    x = int(input())
    if 0 <= x <= 10**6:
        total_positive_numbers += 1
        work_of_numbers *= x
if total_positive_numbers == 0:
    print('NO')
else:
    print(total_positive_numbers, work_of_numbers, sep = '\n')