#!/usr/bin/python3
"""module for class student"""
class Student:
    """a student class"""
    def __init__(self, first_name, last_name, age):
        """intitializer"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance 
        (same as 8-class_to_json.py):
        """
        new_dict = {}
        if (attrs is not None):
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance."""
        for i in self.__dict__:
            if i in json:
                self.__dict__[i] = json[i]
