#!/usr/bin/env python3

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'Фильмы ужасов смотреть онлайн',
    'Смотреть мелодрамы бесплатно без регистрации',
    'Пришли вышли пришли вышли'
]
a = []
count = 0
for text in queries:
    a.append(len(text.split()))
    print(len(text.split()), end=" ")
    count += 1
print()
print("Всего элементов", count, "Список количества слов в предложениях", a, sep="\n")

set_element = set(a)
print("Элементы множества")
buf = list(set_element)
buf.sort()
print(buf)

count_word = []
for i in set_element:
    count_word.append(a.count(i))

print("Количество предложений с n слов")
print(count_word)
j = 0
while j < len(set_element):
    print(f"Поисковых запросов, содержащих {buf[j]} слов(а):", count_word[j])
    j += 1
