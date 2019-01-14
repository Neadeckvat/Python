__author__ = "Виталий Варщук"

# Задание-1
# Написать программу для распаковки файлов в корневую из всех
# папок с расширениями (код взять с урока) и папки удалить

import tkinter.filedialog
from tkinter import Tk
import os


def create_dir_path():
    root = Tk()
    new_dir_path = tkinter.filedialog.askdirectory()
    root.destroy()
    return new_dir_path


print("\nЗадание-1")

command = input("1 - Собрать\n2 - Разобрать\nВведите команду: ")

if command == '1':
    dir_path = create_dir_path()

    files = os.listdir(dir_path)

    exts = []

    for i in files:
        if "." in i:
            exts.append(os.path.splitext(i)[1])

    for i in set(exts):
        if not os.path.exists(os.path.join(dir_path, i)):
            os.mkdir(os.path.join(dir_path, i))

    for file in files:
        destination = os.path.splitext(file)[1]
        os.rename(os.path.join(dir_path, file), os.path.join(dir_path, destination, file))

elif command == '2':
    dir_path = create_dir_path()

    folders = list(os.walk(dir_path))[0][1]

    for i in range(len(folders)):
        if folders[i][0] == '.':
            files = [file for file in os.listdir(os.path.join(dir_path, folders[i]))]
            for file in files:
                os.rename(os.path.join(dir_path, folders[i], file), os.path.join(dir_path, file))
            os.rmdir(os.path.join(dir_path, folders[i]))
