#!/usr/bin/python3
"""printing the alphabet in rev order alternating beetween upper and lower case BTW i love python"""
i = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - i)), end="")
    i = 32 if i == 0 else 0

