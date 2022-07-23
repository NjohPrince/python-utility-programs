#!/usr/bin/env python

"""main.py: functions in python"""

__author__ = "Njoh Noh Prince Junior"
__copyright__ = "Copyright 2022"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Njoh Noh Prince Junior"
__email__ = "jufredprince@gmail.com"

# program starts here - igonore what is above

# function definition


def print_message():
    print("Hello world!")
    
# python lambda function
calculate = lambda a,b: (a*b)+2

# calling the function
print_message()

# executing lambda function
print(calculate(4, 5))

# another function calling print_message function


def main():
    print_message()


# pythons main function -use when the execution flow of the program is to be controlled
if __name__ == "__main__":
    main()
