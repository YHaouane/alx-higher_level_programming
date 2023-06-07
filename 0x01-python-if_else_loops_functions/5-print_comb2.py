#!/usr/bin/python3
"""program that prints numbers from 0 to 99 , with x the number to be printed"""
for x in range(100):
    print('{:02d}'.format(x), end=', ' if x != 99 else '\n')

