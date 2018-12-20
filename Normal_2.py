__author__ = "Варщук Виталий"

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4] Результат: [3, 5, 2]

print('\nЗадание-1')

import math

array = [2, -5, 8, 9, -25, 25, 4]
new_array = []

for i in array:
    if  i > 0 and math.sqrt(i) % 1 == 0:
        new_array.append(int(math.sqrt(i)))
print(new_array)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

print('\nЗадание-2')

date = '02.11.2013'
date = date.split('.')
print(date)

new_date = ''

dd = {'01': 'первое',
      '02': 'второе',
      '03': 'третье',
      '04': 'четвертое',
      '05': 'пятое',
      '06': 'шестое',
      '07': 'седьмое',
      '08': 'восьмое',
      '09': 'девятое',
      '10': 'десятое',
      '11': 'одиннадцатое',
      '12': 'двенадцатое',
      '13': 'тринадцатое',
      '14': 'четырнадцатое',
      '15': 'пятнадцатое',
      '16': 'шестнадцатое',
      '17': 'семнадцатое',
      '18': 'восемнадцатое',
      '19': 'девятнадцатое',
      '20': 'двадцать(ое)',
      '30': 'тридцать(ое)'}

mm = ['января',
      'февраля',
      'марта',
      'апреля',
      'мая',
      'июня',
      'июля',
      'августа',
      'сентября',
      'октября',
      'ноября',
      'декабря']

for i in dd.keys():
    if int(date[0]) <= 20 or int(date[0]) == 30:
        if i == date[0]:
            new_date = dd[i]
    elif 20 < int(date[0]) < 30:
        if int(i) == int(date[0][1]):
            new_date = dd['20'] + ' ' + dd[i]
    elif  int(date[0]) == 31:
        if int(i) == int(date[0][1]):
            new_date = dd['30'] + ' ' + dd[i]

for i in range(len(mm)):
    if int(i + 1) == int(date[1]):
        new_date += ' ' + mm[i]

print(f'{new_date} {date[2]} года')

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

print('\nЗадание-3')

import random

n = int(input("Введите количество элементов в списке: "))

numbers = []

for i in range(n):
    numbers.append(random.randint(-100, 100))
print(numbers)