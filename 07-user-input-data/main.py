#!/usr/bin/env python

"""main.py: getting a users input in python"""

__author__ = "Njoh Noh Prince Junior"
__copyright__ = "Copyright 2022"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Njoh Noh Prince Junior"
__email__ = "jufredprince@gmail.com"

# program starts here - igonore what is above

# getting the users input -thus allowing the user to store his own data
# in a variable [username]
username = input("Enter your name: ")

# displaying a suitable message using f string
print(f"Your username is {username}")

# displaying using format method
print("Your username is {}".format(username))

# displaying using string concatenation -more of this on the next module
print("Your username is " + username)
