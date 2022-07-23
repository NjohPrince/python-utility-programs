#!/usr/bin/env python

"""main.py: comments in python"""

__author__ = "Njoh Noh Prince Junior"
__copyright__ = "Copyright 2022"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Njoh Noh Prince Junior"
__email__ = "jufredprince@gmail.com"

# program starts here - igonore what is above

# 1. Generally comments look like this ✌ Single Line Comments

# print("This will never be printed. Will be ignored during execution.")
print("I will be printed!")

# 2. Block comments

# Hello this is just a random way of displaying very long descriptive
# message. This comment style is a block comment could be longer than
# this depending on what the situation might be.

# 3. Inline Comments

print("Yeah")  # This piece of code prints Yeah
x = 8  # Initialize x with an arbitrary number

# 4. Using DocStrings


def function(num_one, num_two):
    """function(num_one, num_two) -> adds two numbers"""
    return num_one + num_two


# 5. Multiple line DocStrings

def function(num_one, num_two):
    """ function(num_one, num_two) -> adds two numbers
    a: integer
    b: integer
    """
    return num_one + num_two
