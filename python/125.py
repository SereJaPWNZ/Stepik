# Количество пятерок

# На вход программе подается последовательность целых чисел от 1 до 5, характеризующее оценку ученика, каждое число на отдельной строке. Концом последовательности является любое отрицательное число, либо число большее 5. Напишите программу, которая выводит количество пятерок.
# Формат входных данных
# На вход программе подается последовательность чисел, каждое число на отдельной строке.
# Формат выходных данных
# Программа должна вывести количество пятерок.

rating, count = int(input()), 0
while -1 < rating < 6:
    if rating == 5:
        count +=1
    rating= int(input())
print(count)