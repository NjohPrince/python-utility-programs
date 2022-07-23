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

# if statements
num_one = 20
num_two = 30

if num_one > num_two:
    print(f"{num_one} is greater than {num_two}")
else:
    print(f"{num_two} is greater than {num_one}")

# getting users input
num_one = input("\nEnter a number: ")
num_two = input("Enter another number: ")

if num_one > num_two:
    print(
        f"\nYour first number {num_one} is greater than the second {num_two}")
elif num_one == num_two:
    print(f"Both {num_one} and {num_two} are equal.")
else:
    print(f"Your second number {num_two} is greater than the first {num_one}")
