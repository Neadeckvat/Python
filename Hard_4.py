__author__ = "Виталий Варщук"

import pprint

# Задание-1
# Куб состоит из n^3 прозрачных и непрозрачных элементарных кубиков. Имеется ли хотя бы один просвет
# по каждому из трех измерений?
# Если это так, вывести координаты каждого просвета. Куб задается трехмерной матрицей из 0 и 1.

print("\nЗадание-1")

# Задание-2
# Дан pwd.txt с логинами и паролями. Найдите топ10 самых популярных паролей.

print("\nЗадание-2")


def read_file(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        return [s.rstrip().split(';') for s in file.readlines()]


def find_passwords(list_passwords):
    statistic = {}
    passwords = [i[1] for i in list_passwords]
    for s in passwords:
        if s in statistic:
            statistic[s] += 1
        else:
            statistic[s] = 1
    return statistic

def top_10_pass(statistic):
    # sorted(statistic.items(), key=lambda item: item[1])
    top = []
    sort_statistic = sorted(statistic.items(), key=lambda item: item[1])
    for i in range(len(sort_statistic)):
        if i >= (len(sort_statistic) - 10):
            top.append(sort_statistic[i])
    return top


logins_passwords = read_file('pwd.txt')
statistic = find_passwords(logins_passwords)
pprint.pprint(top_10_pass(statistic))

# Задание-3
# Пользователь вводит положительное целое число больше 1
# Нужно создать квадратную матрицу этого размера и по спирали заполнить её числами
# матрица 5 на 5:
#  1  2  3  4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9
# матрица 3 на 3:
# 1 2 3
# 8 9 4
# 7 6 5

print("\nЗадание-3")
