#!/usr/bin/python3
"""moodule for write to a file"""
def write_file(filename="", text=""):
    """
    a function that writes a string to a text file (UTF8) 
    and returns the number of characters written:
    """
    with open(filename, 'w') as F:
        return F.write(text)
