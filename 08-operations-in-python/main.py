#!/usr/bin/env python

"""main.py: Operations in python"""

__author__ = "Njoh Noh Prince Junior"
__copyright__ = "Copyright 2022"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Njoh Noh Prince Junior"
__email__ = "jufredprince@gmail.com"

# program starts here - igonore what is above

# Python has a handful of operators

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# Some arithmetic operators
print(4 + 5)  # 9 -addition
print(10 * 6)  # 60 -multiplication
print("Njoh Noh" + " Prince Junior")  # string concatenation
print(190 - 75)  # 115 -subtraction
print(2 ** 3)  # 8 -exponential

# Some assignment operators
first_name = "Njoh Noh"  # assigns Njoh Noh to the variable first_name
x = 10  # assigns 10 to variable x
x += 2  # assigns x+2 to x -also same as x = x+2
x **= 3  # x = x**3

# Some comparison operators
x = 9  # simply assigning value 9 to x
y = 20  # assigning value 20 to y

# can be tested using print
# print(x == y)
x == y  # compares if x equals y
x > y  # greater than comparison
x < y  # less than comparison
x != y  # not equal to
x <= y  # less than or equal to

# Some logical operators
# can be tested using print
# print(x < 5 and y > 10)
x < 5 and y > 10  # and logical operator
x or y  # or logical operator
not(x > 20)  # not logical operator

# Some identity operators

# a sequence of numbers is needed
y = [5, 6, 7, 3, 10, 75]

print(x is y)  # returns True if both variables are the same object	x is y
print(x is not y)  # returns True if both variables are not the same object

# Some membership operators
print(x in y)  # checks is x exists within a given sequence y
print(x not in y)  # checks is x is not within a given sequence y

# Bitwise operators
# Bitwise operators are mostly used to compare or work with binary numbers:
x = 1001
y = 10

print(x | y)  # Sets each bit to 1 if one of two bits is 1
print(x & y)  # Sets each bit to 1 if both bits are 1
