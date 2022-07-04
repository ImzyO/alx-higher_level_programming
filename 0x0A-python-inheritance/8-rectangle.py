#!/usr/bin/python3
"""module Rectnagle"""
class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry, file 7"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
