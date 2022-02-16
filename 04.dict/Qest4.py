#!/usr/bin/env python3

stats = {'facebook': 55,
         'yandex': 115,
         'vk': 120,
         'google': 99,
         'email': 142,
         'ok': 98}

a = list(stats.values())
a.sort()
b = max(a)

for i in stats.keys():
    if b == stats[i]:
        print("Максимальный объем продаж на рекламном канале:", i)
