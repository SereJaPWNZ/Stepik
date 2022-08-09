# Напишите программу, которая считывает целое число и выводит соответствующую ему римскую цифру. Если число находится вне диапазона 1-10, то программа должна вывести текст «ошибка».
# В таблице приведены римские цифры для чисел от 1 до 10.
number = int(input())
if 1 <= number <= 10:
    if 1<= number <= 3:
        print(number*'I')
    elif number == 4:
        print('IV')
    elif number == 5:
        print('V')
    elif number == 6:
        print('VI')
    elif number == 7:
        print('VII')
    elif number == 8:
        print('VIII')
    elif number == 9:
        print('IX')
    elif number == 10:
        print('X')
else:
    print('ошибка')