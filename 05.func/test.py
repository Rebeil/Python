#!/usr/bin/env python3

documents = [
    {'type': 'passport',
     'number': '2207 876234',
     'name': 'Василий Гупкин'},
    {'type': 'invoice',
     'number': '11-2',
     'name': 'Геннадий Покемонов'},
    {'type': 'insurance',
     'number': '10006',
     'name': 'Аристарх Павлов'}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def press_l():#переписать
    buf1: list[str] = []

    for i in directories:
        buf1.append(i)

    for i in documents:
        print("№: ", i['number'], ", ", "тип: ", i['type'],
              ", ", "владелец: ", i['name'], ", ", "полка хранения: ", buf1.pop(0), sep='')


# ad
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
    print(directories)
    press_l()
else:
    print("Такой полки не существует. Добавьте полку командой as.")
    print("Текущий список документов:")
    press_l()
