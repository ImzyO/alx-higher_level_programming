#!/usr/bin/python3
"""module of same class or inherit from specified class"""
def is_kind_of_class(obj, a_class):
    """method function is_kind_of_class with attribute a_class"""
    # Returns True if obj is an instance of
    # or if the object is an instance of a class that inherited from
    # the specified class, otherwise False
    return isinstance(obj, a_class)
