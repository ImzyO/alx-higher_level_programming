#!/usr/bin/python3
"""module with method is same class"""
    def is_same_class(obj, a_class):
        """
        a function that returns True if the object is exactly
        an instance of the specified class ; otherwise False
        """
        return True if obj is type(a_class) else False
