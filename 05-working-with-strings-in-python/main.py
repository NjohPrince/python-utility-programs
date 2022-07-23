#!/usr/bin/env python

"""main.py: working with strings in python"""

__author__ = "Njoh Noh Prince Junior"
__copyright__ = "Copyright 2022"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Njoh Noh Prince Junior"
__email__ = "jufredprince@gmail.com"

# program starts here - igonore what is above

print(type('Hellloooooo'))  # str

username = "TheUnicornDev"

print(username)  # TheUnicornDev
print(len(username))  # 13 -length of characters in username
print(username.capitalize())  # Theunicorndev

# indexing strings
# index starts from 0

# T -> 0
# h -> 1
# e -> 2
# U -> 3
# n -> 4
# i -> 5
# c -> 6
# o -> 7
# r -> 8 -> -5
# n -> 9 -> -4
# D -> 10 -> -3
# e -> 11 -> -2
# v -> 12 -> -1

print(username[4])  # n -character at 4th index, 5th position
print(username[-1])  # negative indexing from right to left

# NOTE: PYTHON STRINGS ARE IMMUTABLE
# HENCE CAN NOT CHANGE THE ELEMENT WITHIN A GIVEN POSITION
# WITHIN A STRING
# the line below will throw an error

# username[0] = 'D'

# creates a list seprated by the given character['The', 'nicornDev']
print(username.split('U'))

print(username.count('r'))  # count occurence of given character

# slicing strings

print(username[:])  # TheUnicornDev
print(username[1:])  # theUnicornDev -from position 1 to the right
print(username[:1])  # T -from position 1 to the left
# TheUnicornDev -prints but does not reverse the order of characters
print(username[::1])
print(username[::-1])  # reverses the string
print(username[0:10:2])  # [ start : end : step ]

# Example string methods in python

#  capitalize() - Converts the first character to upper case
#  casefold() - Converts string into lower case
#  center() - Returns a centered string
#  count() -  Returns the number of times a specified value occurs in a string
#  encode() - Returns an encoded version of the string
#  endswith() - Returns true if the string ends with the specified value
#  expandtabs() - Sets the tab size of the string
#  find() - Searches the string for a specified value and returns the position of where it was found
#  format() - Formats specified values in a string
#  format_map() - Formats specified values in a string
#  index() -  Searches the string for a specified value and returns the position of where it was found
#  isalnum() -  Returns True if all characters in the string are alphanumeric
#  isalpha() -  Returns True if all characters in the string are in the alphabet
#  isdecimal() -  Returns True if all characters in the string are decimals
#  isdigit() -  Returns True if all characters in the string are digits
#  isidentifier() - Returns True if the string is an identifier
#  islower() -  Returns True if all characters in the string are lower case
#  isnumeric() -  Returns True if all characters in the string are numeric
#  isprintable() -  Returns True if all characters in the string are printable
#  isspace() -  Returns True if all characters in the string are whitespaces
#  istitle() -  Returns True if the string follows the rules of a title
#  isupper() -  Returns True if all characters in the string are upper case
#  join() - Joins the elements of an iterable to the end of the string
#  ljust() -  Returns a left justified version of the string
#  lower() -  Converts a string into lower case
#  lstrip() - Returns a left trim version of the string
#  maketrans() -  Returns a translation table to be used in translations
#  partition() -  Returns a tuple where the string is parted into three parts
#  replace() -  Returns a string where a specified value is replaced with a specified value
#  rfind() -  Searches the string for a specified value and returns the last position of where it was found
#  rindex() - Searches the string for a specified value and returns the last position of where it was found
#  rjust() -  Returns a right justified version of the string
#  rpartition() - Returns a tuple where the string is parted into three parts
#  rsplit() - Splits the string at the specified separator, and returns a list
#  rstrip() - Returns a right trim version of the string
#  split() -  Splits the string at the specified separator, and returns a list
#  splitlines() - Splits the string at line breaks and returns a list
#  startswith() - Returns true if the string starts with the specified value
#  strip() -  Returns a trimmed version of the string
#  swapcase() - Swaps cases, lower case becomes upper case and vice versa
#  title() -  Converts the first character of each word to upper case
#  translate() -  Returns a translated string
#  upper() -  Converts a string into upper case
#  zfill() -  Fills the string with a specified number of 0 values at the beginning
