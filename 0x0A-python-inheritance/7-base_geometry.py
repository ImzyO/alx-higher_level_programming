#!/usr/bin/python3
"""module inetegr validator"""
class BaseGeometry:
    """class basegeometry based on file6"""
    def area(self):
        """method calculating area"""
        raise Exception("area() is not implemented")
    #exception handling
    def integer_validator(self, name, value):
        """method that validates if value is int"""
        if type(value) is  not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
