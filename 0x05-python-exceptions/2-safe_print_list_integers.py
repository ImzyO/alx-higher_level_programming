#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    k = 0
    for l in range(0, x):
        try:
            print("{:d}".format(my_list[l]), end="")
            k += 1
        except (TypeError, ValueError):
            pass
        print("")
        return k
