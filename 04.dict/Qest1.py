#!/usr/bin/env python3

ids = {'user1': [213, 213, 213, 15, 213], 
       'user2': [54, 54, 119, 119, 119], 
       'user3': [213, 98, 98, 35]}
a = set()

for v in ids.values():
    for i in v:
        a.add(i)
print(*a)
