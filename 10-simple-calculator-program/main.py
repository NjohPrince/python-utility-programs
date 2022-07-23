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

# creating a dictionary to track chosen operator
match_operators_to_selection = {1: "+", 2: "-", 3: "*", 4: "/"}

# converted input into an integer
operation = int(input("\nSelect an operation: "))

# check if operator is within our available options
if operation not in range(1, 5):
    print("Invalid operator!")
    exit(0)  # exit the program

num_one = int(input("\nEnter a number: "))  # converted input into an integer
# converted input into an integer
num_two = int(input("Enter another number: "))

print(
    f"\nExpression is {str(num_one) + ' ' + match_operators_to_selection[operation] + ' ' + str(num_two)}")

if operation == 1:
    print("\nResult is ", num_one + num_two)
elif operation == 2:
    print("\nResult is ", num_one - num_two)
elif operation == 3:
    print("\nResult is ", num_one * num_two)
elif operation == 4:
    if num_two == 0:  # division by zero error
        print("\nError division by zero is not allowed.")
    else:
        print("\nResult is ", num_one / num_two)
