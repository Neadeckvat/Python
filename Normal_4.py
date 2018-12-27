__author__ = "Виталий Варщук"

# Задание-1:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

print("\nЗадание-1")

import os
import random


def create_new_file(filename):
    with open(filename, 'w', encoding='UTF-8') as file:
        for _ in range(2500):
            file.write(str(random.randint(0, 9)))


def read_file(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        my_string = file.readline()
        return create_number(my_string)


def create_number(my_string):
    string = my_string[0]
    long_string = ''
    longest_string = ''
    for n in range(1, len(my_string)):
        if my_string[n] != string:
            long_string = my_string[n]
        else:
            long_string += my_string[n]
        if len(long_string) > len(longest_string):
            longest_string = long_string
        string = my_string[n]
    return longest_string


create_new_file("For_Normal_4.txt")
print(read_file("For_Normal_4.txt"))


# Задание-2
# Сформировать квадратную матрицу, в каждой строке которой находится ровно один ноль на случайном месте,
# остальные элементы тоже рандомные. Пользователь вводит размер

print("\nЗадание-2")

import pprint
import random

size = int(input("Введите размер матрицы (одним числом): "))

matrix = [[random.randint(1, 9) for _ in range(size)] for _ in range(size)]

for i in matrix:
    num = random.randint(0, len(i)-1)
    i.pop(num)
    i.insert(num, 0)

pprint.pprint(matrix)
