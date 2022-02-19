#!/usr/bin/env python3

import os

print(f"Current workong directory is {os.getcwd()}")

print(os.path.exists('Python'))

#смотрит из текущей директории
print(os.path.exists(os.path.join('0x.', 'lib_os.py')))

#подкаталоги test_dir->level_1->level_2->level_3
os.makedirs(os.path.join('test_dir', 'level_1', 'level_2', 'level_3'))
