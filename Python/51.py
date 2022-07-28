#На вход программе подаётся два целых числа n и k, скорость Зума и Флэша.
#Если Зум быстрее Флэша нужно вывести «NO», если Флэш быстрее Зума нужно вывести «YES», если их скорости равны нужно вывести "Don't know".
speed_n, speed_k = int(input()), int(input())
if speed_n == speed_k:
    print("Don't know")
elif speed_n > speed_k:
    print('NO')
else:
    print('YES')