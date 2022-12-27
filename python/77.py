# Интересное число

# Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней по величине цифре. Напишите программу, которая определяет интересное число или нет. Если число интересное, следует вывести – «Число интересное» иначе «Число неинтересное».
# Формат входных данных
# На вход программе подается целое трехзначное число.
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

a, b, c = input()
max_number = max(int(a), int(b), int(c))
min_number = min(int(a), int(b), int(c))
intermediate_number = (sum([int(a), int(b), int(c)]) - max_number - min_number)
print('Число интересное' if max_number - min_number == intermediate_number else 'Число неинтересное')