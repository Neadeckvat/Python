__author__ = "Варщук Виталий"

# Задача-1 Пользователь вводит текст, необходимо разбить его по словам и выдать статистику по тексту
# 1. Сколько слов в тексте?
# 2. Сколько букв английского алфавита в тексте?

print('\nЗадание-1')

import string

text = input("Введите текст: ")
text = text.lower()

for n in string.punctuation:
    while n in text:
        text = text.replace(n, "")
list_text = text.split(' ')
print(f'В данном тексте {len(list_text)} слов')

while ' ' in text:
    text = text.replace(' ', "")
for word in text:
    if ord(word) < 97 or ord(word) > 122:
        text = text.replace(word, "")
print(f'В данном тексте {len(text)} английских символа(ов)')

# Задача-2 Пользователь вводит два текста, необходимо найти все слова, которые есть в обоих текстах. Без учета регистра

print('\nЗадание-2')

text_1 = input("Введите первый текст: ")
text_1 = text_1.lower()
text_2 = input("Введите второй текст: ")
text_2 = text_2.lower()

words = []

for n in string.punctuation:
    while n in text_1:
        text_1 = text_1.replace(n, "")
    while n in text_2:
        text_2 = text_2.replace(n, "")
list_text_1 = text_1.split(' ')
list_text_2 = text_2.split(' ')

for i in list_text_1:
    for j in list_text_2:
        if i == j:
            if i not in words:
                words.append(i)
print(f'Список слов, присутствующих в обоих текстах:\n{words}')