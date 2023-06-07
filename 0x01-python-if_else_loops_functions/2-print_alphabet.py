#!/usr/bin/python3
"""it will print the alphabet in lowercase not followed by a \n"""

for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
