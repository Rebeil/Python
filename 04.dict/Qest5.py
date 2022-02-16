#!/usr/bin/env python3

my_list = ['a', 'b', 'c', 'd', 'e', 'f']

print(', '.join(str(i) for i in my_list))
dict_ = {my_list[-2]: my_list[-1]}
print(dict_)
my_list.reverse()
for i in my_list[2:]:
    dict_ = {i: dict_}

print(dict_)
