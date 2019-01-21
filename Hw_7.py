__author__ = "Виталий Варщук"

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

import random


class Card:
    def __init__(self):
        self.card = self.create_card()
        self.start = "-" * 26
        self.end = "-" * 26

    def __str__(self):
        return f'{self.start}\n{" ".join(self.card[0])}\n{" ".join(self.card[1])}\n{" ".join(self.card[2])}\n{self.end}'

    def create_card(self):
        kegs_list = self.create_kegs_list()
        num_lines = 3
        len_line = 9
        full_list = [kegs_list[:len_line * 3][i::num_lines] for i in range(num_lines)]
        for line in range(len(full_list)):
            random_nums = [i for i in range(len(full_list[line]))]
            random.shuffle(random_nums)
            for num in random_nums:
                if len(set(full_list[line])) < 7:
                    break
                full_list[line][num] = "  "
        return full_list

    def check_card(self, keg):
        if len(str(keg)) < 2:
            keg = " " + str(keg)
        else:
            keg = str(keg)
        for line in range(len(self.card)):
            for i in range(len(self.card[line])):
                if keg == self.card[line][i]:
                    self.card[line][i] = ' +'
                    return 'Ответ верен'
        return 'Ответ не верен'

    @staticmethod
    def create_kegs_list():
        kegs = [str(i) for i in range(1, 91)]
        for i in range(len(kegs)):
            if len(kegs[i]) < 2:
                kegs[i] = " " + kegs[i]
        random.shuffle(kegs)
        return kegs


class UserCard(Card):
    def __init__(self):
        Card.__init__(self)
        self.start = f'{"-" * 6} Ваша карточка {"-" * 5}'


class ComputerCard(Card):
    def __init__(self):
        Card.__init__(self)
        self.start = f'{"-" * 2} Карточка компьютера {"-" * 3}'


game_kegs = [i for i in range(1, 91)]
random.shuffle(game_kegs)

user = UserCard()
computer = ComputerCard()

for i in range(len(game_kegs)):
    print(f'\nНовый бочонок: {game_kegs[i]} (осталось {len(game_kegs) - i - 1})')
    print(user)
    print(computer)
    answer = input('Зачеркнуть цифру? (y/n): ').lower()
    if answer == "y":
        check = user.check_card(game_kegs[i])
        if check == 'Ответ не верен':
            print(f"\nИгрок проиграл (цифры {game_kegs[i]} нет в ваше карточке)")
            break
    elif answer == "n":
        check = user.check_card(game_kegs[i])
        if check == 'Ответ верен':
            print(f"\nИгрок проиграл (цифра {game_kegs[i]} была в вашей карточке)")
            break
    computer.check_card(game_kegs[i])
    if len(set(user.card[0] + user.card[1] + user.card[2])) == 2:
        print("\nИгрок выйграл")
        break
    if len(set(computer.card[0] + computer.card[1] + computer.card[2])) == 2:
        print("\nКомпьютер выйграл")
        break
