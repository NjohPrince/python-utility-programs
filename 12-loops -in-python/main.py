#!/usr/bin/env python

"""main.py: loops in python"""

__author__ = "Njoh Noh Prince Junior"
__copyright__ = "Copyright 2022"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Njoh Noh Prince Junior"
__email__ = "jufredprince@gmail.com"

# program starts here - igonore what is above

# for loop -example 1
for i in range(1, 6):  # loops from 1 to 5
    print(i)  # will print from 1 to 5

costumes = ['Spidey Wear', 'Hulk Skin', 'Iron Suit', 'Pyjamas']

# example 2 -print each costume in costumes list
for costume in costumes:
    print(costume)

print("\n")

# example 3 -printing by using their indices
for i in range(len(costumes)):
    print(costumes[i])

print("\n")

# while loop

i = 0
while i < 4:
    print(costumes[i])
    i += 1
