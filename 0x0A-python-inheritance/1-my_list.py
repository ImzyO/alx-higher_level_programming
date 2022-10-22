#!/usr/bin/python3
"""module with class MyList"""
class MyList(list):
    """class with method print_sorted"""
    def print_sorted(self):
        """method that sorts a list"""
        print(sorted(self))
