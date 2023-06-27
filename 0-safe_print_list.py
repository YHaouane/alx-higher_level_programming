#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x the element of a list.

    Args:
        my_list (list): list to print elements from.
        x (int):  number of elements of the_list to print.

    Returns:
         number of elements printed.
    """
    counter = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            counter += 1
        except IndexError:
            break
    print("")
    return (counter)
