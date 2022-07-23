#!/usr/bin/env python

"""main.py: structuring and working with large projects in python"""

__author__ = "Njoh Noh Prince Junior"
__copyright__ = "Copyright 2022"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Njoh Noh Prince Junior"
__email__ = "jufredprince@gmail.com"

# program starts here - igonore what is above

import os  # working with the operating system

print(os.getcwd())  # get current working directory

print("\n")
print(os.listdir())  # list all directories within current directory

print("\n")
# changing the current directory -changed to an existing directory in your system
os.chdir('D:\Repositories')

print("\n")
print("Current directory changed to: ", os.getcwd())

for directory in os.listdir():
    print(directory)

    # CAUTION: deleting a directory in python
    # destructive -please be sure when you want to test
    # os.rmdir(directory)

# create a directory
# os.mkdir('tempDir')
