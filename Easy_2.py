__author__ = "Варщук Виталий"

#Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
# Подсказка: воспользоваться методом .format()

print("\nЗадание-1")

fruits = ["яблоко", "банан", "киви", "арбуз"]

for i in range(len(fruits)):
    print(f'{i + 1}. {fruits[i]:>{len(max(fruits))}}')

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

print("\nЗадание-2")

a = ["яблоко", "банан", "киви", "арбуз", 1, 11, 111, 1111, 0.1, 1.01, "яблоко"]
b = ["яблоко", 111, 1.01]

print(f'Первый список: {a}')
print(f'Второй список: {b}')

for i in b:
    for j in a:
        if i == j:
            a.remove(j)
            print(f'Удален элемент: {j}')
print(f'После удаления из первого списка элементов второго: {a}')

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print("\nЗадание-3")

numbers = []
for i in range(10):
    numbers.append(i+1)
print(f'Данный список: {numbers}')

new_numbers = []
for i in numbers:
    if i % 2 == 0:
        new_numbers.append(i / 4)
    else:
        new_numbers.append(i * 2)
print(f'Новый список: {new_numbers}')