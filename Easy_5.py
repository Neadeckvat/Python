__author__ = "Виталий Варщук"

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os


def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)


def delete_folder(path):
    if os.path.exists(path):
        os.rmdir(path)


print("\nЗадание-1")

name_folder = "dir_"

print("1 - Создать папки\n2 - Удалить папки")

command = int(input("Введите номер команды: "))

if command == 1:
    for i in range(1, 10):
        create_folder(name_folder + str(i))
elif command == 2:
    for i in range(1, 10):
        delete_folder(name_folder + str(i))
else:
    print("Вы ввели несуществующую команду")

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print("\nЗадание-2")

folders = [i for i in os.listdir('.') if os.path.isdir(i)]

print(folders)
