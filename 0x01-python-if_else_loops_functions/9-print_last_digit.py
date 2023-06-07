#!/usr/bin/python3
def print_last_digit(number):
    """print the last digit of a number then return it."""
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
