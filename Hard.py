__author__ = "Варщук Виталий"

# Задание-1:
# Пользователь вводит число определите, является ли данное число простым. Делится только на себя и на единицу
print("\nЗадание-1")

num = int(input('Введите целое число: '))
count = 0

if num == 2:
    print(f"Число {num} простое")
elif num % 2 == 0:
    print(f"Число {num} не является простым")
else:
    for k in range(1, num + 1):
        if num % k == 0:
            count += 1
    if count == 2:
        print(f"Число {num} простое")
    else:
        print(f"Число {num} не является простым")

# Задание-2
# Найдите n-ое число Фибоначчи

def fibonachchi(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return (fibonachchi(number - 1) + fibonachchi(number - 2))

print("\nЗадание-2")

number = int(input("Какое число Фибоначчи Вы хотите найти?: "))
answer = fibonachchi(number)

print(f'{number} число Фибоначчи равно: {answer}')

# Задание-3
# Пользователь вводит n и m и нужно вывести на экран:
# AAABBBAAABBBAAABBB
# BBBAAABBBAAABBBAAA
# AAABBBAAABBBAAABBB
# Для этого примера n == 3, m == 3
# где n - это количество строк, m - это кол-во троек ААА в одной строке

print("\nЗадание-3")

n = int(input("Введите количество строк: "))
m = int(input("Введите количество троек ААА в одной строке: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print('BBBAAA' * m)
    else:
        print('AAABBB' * m)