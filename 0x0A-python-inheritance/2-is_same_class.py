#!/usr/bin/python3
"""module with method is same class"""
class a_class:
    """
    class that returns True if object  is exactly an instance of
    the specified class: else false
    """
    def is_same_class(obj, a_class):
        return type(obj) is a_class
