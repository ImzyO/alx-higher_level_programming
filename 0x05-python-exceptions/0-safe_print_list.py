#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in my_list:
        try:
             x += 1
        except ValueError:
             print("my_list[i]")
