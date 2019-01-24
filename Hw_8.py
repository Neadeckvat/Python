__author__ = "Варщук Виталий"

# 1. Дано предложение. Заменить группы пробелов одиночными, крайние пробелы удалить.
# Все слова перевести в нижний регистр, первые буквы сделать заглавными.


def change_text(txt):
    txt = txt.strip()
    txt_lst = txt.split(" ")
    while '' in txt_lst:
        txt_lst.remove('')
    txt = ' '.join(txt_lst).title()
    return txt


sentence = input("Введите предложение: ")

sentence = change_text(sentence)

print(sentence)

# 2. Дана строка. Заменить все ссылки и email на ***** (количество звездочек равно длине заменяемого фрагмента).
# Примеры ссылок: www.site.com, http://site.com и т.п.


def check_url(txt, url_lst):
    txt_lst = txt.split(' ')
    for n in range(len(txt_lst)):
        for url in url_lst:
            if txt_lst[n].find(url) == 0:
                txt_lst[n] = '*' * len(txt_lst[n])
    txt_lst = ' '.join(txt_lst)
    return txt_lst


def check_mail(txt):
    txt_lst = txt.split(' ')
    for n in range(len(txt_lst)):
        if "@" in txt_lst[n] and "." in txt_lst[n]:
            txt_lst[n] = '*' * len(txt_lst[n])
    txt_lst = ' '.join(txt_lst)
    return txt_lst


url_list = ['http://', 'https://', 'www.']

text = input("Введите текст: ")
text = check_url(text, url_list)
text = check_mail(text)
print(text)

# 3. Пользователь бесконечно вводит e-mail адреса. Вывести только те, которые не повторяются.


def check_e_mail(e_mail, e_mail_lst, del_lst):
    if e_mail in del_lst:
        if e_mail in e_mail_lst:
            e_mail_lst.remove(e_mail)
        return e_mail_lst, del_lst
    else:
        del_lst.append(e_mail)
        e_mail_lst.append(e_mail)
        return e_mail_lst, del_lst


e_mail_list = []
del_list = []

while True:
    new_e_mail = input("Введите e-mail адрес: ")
    if "@" not in new_e_mail:
        continue
    e_mail_list, del_list = check_e_mail(new_e_mail, e_mail_list, del_list)
    print(e_mail_list)
