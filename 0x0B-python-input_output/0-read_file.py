#!/usr/bin/python3
"""this is a module for read file"""
def read_file(filename=""):
    """ a function that reads a text file (UTF8) and prints it to stdout:"""
    with open(filename, "r", encoding="UTF-8") as F:
        print(F.read(), end="")
