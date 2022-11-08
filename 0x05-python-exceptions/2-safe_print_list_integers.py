#!/usr/bin/python3
""" Print and count integers"""


def safe_print_list_integers(my_list=[], x=0):
    """first x elements"""
    i = 0
    count = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            pass
        else:
            count += 1
        finally:
            i += 1

    print()
    return count
