__author__ = "Виталий Варщук"

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

print("\nЗадание-1")


def my_round(number, ndigits):
    int_number = number // 1
    float_number = number - int_number
    end_number = ((float_number * 10 ** (ndigits + 1)) // 1) - ((float_number * 10 ** (ndigits)) // 1) * 10
    if end_number >= 5:
        float_number = ((float_number * 10 ** ndigits // 1) + 1) / (10 ** ndigits)
    elif end_number < 5:
        float_number = (float_number * 10 ** ndigits // 1) / (10 ** ndigits)
    else:
        pass
    return int_number + float_number


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

print("\nЗадание-2")


def lucky_ticket(ticket_number):
    num_1 = 0
    num_2 = 0
    for i in str(ticket_number)[:len(str(ticket_number)) // 2]:
        num_1 += int(i)
    for i in str(ticket_number)[len(str(ticket_number)) // 2:]:
        num_2 += int(i)
    if num_1 == num_2:
        return "Билет счастливый"
    else:
        return "Билет обычный"


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))