# Все вместе

# Дано натуральное число. Напишите программу, которая вычисляет:
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.
# Формат входных данных 
# На вход программе подается одно натуральное число.
# Формат выходных данных
# Программа должна вывести значения указанных величин в указанном порядке.

n, sum_numbers, count_numbers, the_work_of_its_numbers = int(input()), 0, 0, 1
dump_n= n
while n != 0:
    temp_number = n % 10
    sum_numbers += temp_number
    count_numbers += 1
    the_work_of_its_numbers *= temp_number 
    the_arithmetic_mean = sum_numbers / count_numbers
    n //= 10
first_number =  temp_number
sum_first_and_last_digit = first_number + dump_n % 10
print(sum_numbers, count_numbers, the_work_of_its_numbers, the_arithmetic_mean, first_number, sum_first_and_last_digit, sep = '\n')