# В купейном вагоне имеется 99 купе с четырьмя местами для пассажиров в каждом. Напишите программу, которая определяет номер купе, в котором находится место с заданным номером (нумерация мест сквозная, начинается с 11).
# link https://ucarecdn.com/759a79a5-79d0-489a-8d2c-cc337483d2af/
# Формат входных данных
# На вход программе подаётся целое число – место с заданным номером в вагоне.
# Формат выходных данных
# Программа должна вывести одно число – номер купе, в котором находится указаное место.

i = int(input())
d = -i // 4
print(-d)