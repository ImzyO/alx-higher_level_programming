#!/usr/bin/python3
"""module for student to JSON with filter"""
class Student:
    """a student class"""
    def __init__(self, first_name, last_name, age):
        """initializes class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a
        Student instance (same as 8-class_to_json.py)
        """
        new = {}
        if (att is not None):
            for i in att:
                if i in self.__dict__:
                    new[i] = self.__dict__[i]
            return new
        else:
            return self.__dict__
