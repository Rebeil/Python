#!/usr/bin/env python3

documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def press_p():
    print("Введите номер документа:")
    number = str(input())
    buf = -1
    for users in documents:
        if users['number'] == number:
            buf = users
    if buf != -1:
        print("Владелец документа:", buf['name'])
    else:
        print("Документ не найден в базе")


def press_s():
    print("Введите номер документа:")
    user = str(input())
    buf = -1

    for i in directories:
        for j in directories[i]:
            if j == user:
                buf = i

    if buf != -1:
        print("Документ хранится на полке:", buf)
    else:
        print("Документ не найден в базе")


def press_l():
    buf: list[str] = []

    for i in directories:
        buf.append(i)

    for i in documents:
        print("№: ", i['number'], ", ", "тип: ", i['type'],
              ", ", "владелец: ", i['name'], ", ", "полка хранения: ", buf.pop(0), sep='')


def press_ads():
    print("Введите номер полки:")
    user = str(input())
    flag = False
    for i in directories.keys():
        if user == i:
            flag = True
            break

    if not flag:
        directories[user] = []
        print("Полка добавлена. Текущий перечень полок:", *directories.keys(), end="")
        print(".")
    else:
        print("Такая полка уже существует. Текущий перечень полок:", *directories.keys(), end="")
        print(".")


def press_ds():
    user = input()
    buf = -1
    flag = False

    # with goto will be simplest
    for i in directories.keys():
        if user == i:
            flag = True

    if flag:
        for i in directories.keys():
            if user == i:
                if not directories[i]:
                    buf = i
                    break
        if buf != -1:
            del directories[buf]
            print("Полка удалена. Текущий перечень полок:", *directories.keys())
        else:
            print("На полке есть документа, удалите их перед удалением полки. Текущий перечень полок:",
                  *directories.keys())
    else:
        print("Такой полки не существует. Текущий перечень полок: 1, 2, 3.")


def press_ad():
    print("Введите номер документа:")
    user = input()
    print("Введите тип документа:")
    user1 = input()
    print("Введите владельца документа:")
    user2 = input()
    print("Введите полку для хранения:")
    user3 = input()

    if user3 in list(directories.keys()):
        documents.append({'number': user,
                          'type': user1,
                          'name': user2})

        directories[user3].append(user)
        print("Документ добавлен. Текущий список документов:")
        press_l()
    else:
        print("Такой полки не существует. Добавьте полку командой as.")
        print("Текущий список документов:")
        press_l()


def press_d():
    pass


while 1:
    print("Введите команду:")
    user_input = input()
    if user_input != 'q':
        if user_input == 'p':
            press_p()
        elif user_input == 's':
            press_s()
        elif user_input == 'l':
            press_l()
        elif user_input == 'ads':
            press_ads()
        elif user_input == 'ds':
            press_ds()
        elif user_input == 'ad':
            press_ad()
        else:
            print("нет такой команды")
    else:
        print("Exit")
        break
