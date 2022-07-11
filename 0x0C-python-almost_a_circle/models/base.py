#!/usr/bin/python3
"""module for base.py"""
from json import loads, dumps
"""import module json, imports loads and dumps"""
import csv

class Base:
    """a class named Base"""
    __nb_objects = 0
    """private class attribute"""
    def __init__(self, id=None):
        """initializes class Base"""
        #loop statement
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
