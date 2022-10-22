#!/usr/bin/python3
"""module with a method inherits_from, a subclass"""
def inherits_from(obj, a_class):
    """
    a function that returns True if the object is an instance of
    a class that inherited (directly or indirectly) from the specified class ; otherwise False
    """
    if type(obj) is not a_class:
        return isinstance(obj, a_class)
    else:
        False
