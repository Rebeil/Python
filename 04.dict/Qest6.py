#!/usr/bin/env python3

countries_temperature = [
    ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Germany', [57.2, 55.4, 59, 59, 53.6]],
    ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]

#print(countries_temperature[1][1])
a = []
# print(len(countries_temperature))

i = 0
while i < len(countries_temperature):
    j = 0
    summ = 0

    while j < len(countries_temperature[i][1]):
        summ += countries_temperature[i][1][j]
        j += 1
    a.append(((summ / len(countries_temperature[i][1])) - 32) * 5/9)
    i += 1

i = 0
while i < len(countries_temperature):
    print(countries_temperature[i][0], a[i])
    i += 1
