#!/usr/bin/env python

"""main.py: handling errors in python"""

__author__ = "Njoh Noh Prince Junior"
__copyright__ = "Copyright 2022"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Njoh Noh Prince Junior"
__email__ = "jufredprince@gmail.com"

# program starts here - igonore what is above

# try except
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Error! That was no valid number.  Try again...")
    finally:
        print("Executing finally clause")  # will run

# determining the error type in python
# try:
#     x = 1/0
# except Exception as exception:
#     error = type(exception)
#     print(error)  # <class 'ZeroDivisionError'>

# extracting the error message
try:
    x = 1/0
except Exception as ex:
    templateError = "\nAn exception of type {0} occurred during execution. Arguments:\n{1!r}"
    message = templateError.format(type(ex).__name__, ex.args)
    print(message)
