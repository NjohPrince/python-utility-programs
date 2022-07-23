#!/usr/bin/env python

"""main.py: simple calculator in python"""

__author__ = "Njoh Noh Prince Junior"
__copyright__ = "Copyright 2022"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Njoh Noh Prince Junior"
__email__ = "jufredprince@gmail.com"

# program starts here - igonore what is above

print("Hello, welcome to a simple calculator made with python!")
username = input("Please enter your name ")

# \n escape to the next line
print("\n{} welcome to simplo-calculator.\n".format(username))

print("Operation Set:")
print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division")

operation = input("Select an operation: ")
num_one = input("\nEnter a number: ")
num_two = input("Enter another number")

print(f"\nExpression is {num_one + ' ' + operation + ' ' + num_two}\n")

print(f"\nResult is \n")
