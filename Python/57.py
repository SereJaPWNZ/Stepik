# Красный, синий и желтый называются основными цветами, потому что их нельзя получить путем смешения других цветов. При смешивании двух основных цветов получается вторичный цвет:
# если смешать красный и синий, то получится фиолетовый;
# если смешать красный и желтый, то получится оранжевый;
# если смешать синий и желтый, то получится зеленый.
# Напишите программу, которая считывает названия двух основных цветов для смешивания. Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый», то программа должна вывести сообщение об ошибке. В противном случае программа должна вывести название вторичного цвета, который получится в результате.
# Формат входных данных
# На вход программе подаются две строки, каждая на отдельной строке.
# Формат выходных данных
# Программа должна вывести полученный цвет смешения либо сообщение «ошибка цвета», если введён был не цвет.
# Примечание 1. Если смешать красный и красный, то получится красный и т.д.

color_1, color_2 = input(), input()
if color_1 in ['красный', 'синий', 'желтый'] and color_2 in ['красный', 'синий', 'желтый']:
    if color_1 == color_2:
        print(color_2)
    elif color_1 in ['красный', 'синий'] and color_2 in ['красный', 'синий']:
        print('фиолетовый')
    elif color_1 in ['красный', 'желтый'] and color_2 in ['красный', 'желтый']:
        print('оранжевый')
    elif color_1 in ['синий', 'желтый'] and color_2 in ['синий', 'желтый']:
        print('зеленый')
else:
    print('ошибка цвета')