#!/usr/bin/env python

"""main.py: converting from one datatype to another in python"""

__author__ = "Njoh Noh Prince Junior"
__copyright__ = "Copyright 2022"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Njoh Noh Prince Junior"
__email__ = "jufredprince@gmail.com"

# program starts here - igonore what is above

from ast import Num


data = "123"

print(type(data))  # <class 'str'>

print(int(data))  # 123
print(type(int(data)))  # <class 'int'>

print(float(data))  # 123.0

character = 'c'

# converts and displays the ascii representation of the string
print(ord(character))

python_string = 'python'
converted_to_tuple = tuple(python_string)
# ('p', 'y', 't', 'h', 'o', 'n')
print("string converted into tuple:  ", converted_to_tuple)
