#!/usr/bin/python3
"""module for student to JSON"""
class Student:
    """class for students"""
    def __init__(self, first_name, last_name, age):
        """class student initialized by this method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self):
        """
        that retrieves a dictionary representation of a Student
        instance (same as 8-class_to_json.py)
        """
        return self.__dict__
