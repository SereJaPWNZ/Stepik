# What's Your Name?

# Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:
# «Hello [введенное имя] [введенная фамилия]! You just delved into Python».
# Формат входных данных
# На вход программе подаётся две строки (имя и фамилия), каждая на отдельной строке.
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
# Примечание. Между firstname lastname вставьте пробел =)

# var1
firstname, lastname = input(), input()
print(f'Hello', firstname, lastname + '! You just delved into Python')

# var2
firstname, lastname = input(), input()
print(f'Hello {firstname} {lastname}! You just delved into Python')