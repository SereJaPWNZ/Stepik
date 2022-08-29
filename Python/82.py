# Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
# Формат входных данных
# На вход программе подаётся названия трех городов, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.
# Примечание. Гарантируется, что длины названий всех трех городов различны.

city_name_1, city_name_2, city_name_3 = input(), input(), input()
len_c1 = len(city_name_1) 
len_c2 = len(city_name_2)
len_c3 = len(city_name_3)
Max_len = max(len_c1, len_c2, len_c3)
Min_len = min(len_c1, len_c2, len_c3)
if Min_len == len_c1:
    print(city_name_1)
if Min_len == len_c2:
    print(city_name_2)
if Min_len == len_c3:
    print(city_name_3)
if Max_len == len_c1:
    print(city_name_1)
if Max_len == len_c2:
    print(city_name_2)
if Max_len == len_c3:
    print(city_name_3)