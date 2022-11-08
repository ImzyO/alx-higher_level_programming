#!/usr/bin/python3
"""module that has the method lookup"""


def lookup(obj):
    """returns the list of availableattribute, methods of an object"""
    return dir(obj)
