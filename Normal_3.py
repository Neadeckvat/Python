__author__ = "Виталий Варщук"

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

print('\nЗадание-1')


def fibonacci(n, m):
    fib = []
    for i in range(n, m + 1):
        a = 0
        b = 1
        if i == 1:
            fib.append(a)
        elif i == 2:
            fib.append(b)
        else:
            for j in range(i - 2):
                c = a + b
                a = b
                b = c
            fib.append(b)
    return fib


print(fibonacci(1, 11))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

print('\nЗадание-2')


def sort_to_max(origin_list):
    count = len(origin_list)-1
    while count != 0:
        for n in range(len(origin_list) - 1):
            if origin_list[n] > origin_list[n + 1]:
                temp_1 = origin_list[n]
                temp_2 = origin_list[n + 1]
                origin_list.insert(n, temp_2)
                origin_list.pop(n + 1)
                origin_list.insert(n + 1, temp_1)
                origin_list.pop(n + 2)
        count -= 1
    print(origin_list)


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
sort_to_max([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

print('\nЗадание-3')


def test_func(arg):
    if arg > 0:
        return True
    else:
        return False


def my_filter(func, object):
    new_object = []
    if func == None:
        for n in object:
            if bool(n) == True:
                new_object.append(n)
    else:
        for n in object:
            if func(n) == True:
                new_object.append(n)
    return new_object


array = [2, 0, -12, 2.5, 20, -11, 0, 0, 0, 0]
print(my_filter(None, array))
print(my_filter(test_func, array))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

print('\nЗадание-4')


def len_side(point_1, point_2):
    '''Вычисляет длину стороны параллелограмма'''
    return ((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2) ** (0.5)


def center_diagonal(point_1, point_2):
    '''Вычисляет точку пересечения диагоналей параллелограмма'''
    return (((point_1[0] + point_2[0]) / 2) , ((point_1[1] + point_2[1]) / 2))


def parallelogram(A, B, C, D):
    if len_side(A, B) == len_side(C, D) and len_side(B, C) == len_side(D, A) and center_diagonal(A, C) == center_diagonal(B, D):
        return "Данные точки являются вершинами параллелограмма"
    else:
        return "Данные точки не являются вершинами параллелограмма"


A = (-3, 11)
B = (12, -4)
C = (1, -7)
D = (-14, 8)
print(parallelogram(A, B, C, D))