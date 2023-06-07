#!/usr/bin/python3
"""printing all the alphabet except q and e"""

for letter in range (97, 123):
    if chr(letter) is not 'q' and chr(letter) is not 'e':
        print("{}".format(chr(letter)),end="")
