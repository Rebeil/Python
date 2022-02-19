#!/usr/bin/env python3

import os

print(f"Current workong directory is {os.getcwd()}")

print(os.path.exists('Python'))

print(os.path.exists(os.path.join('0x.', 'lib_os.py')))
