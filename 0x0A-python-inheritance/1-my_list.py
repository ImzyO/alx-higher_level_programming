#!/usr/bin/python3
"""module with class MyList"""
class MyList(list):
    """class with method print_sorted"""
    def print_sorted(self):
        """method that sorts a list"""
        super().__init__(self)
        """initialization"""
        sortit = list.sorted
        return sortit
