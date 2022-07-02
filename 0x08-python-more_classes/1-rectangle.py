#!/usr/bin/python
"""
module for only rectangle use
"""
class Rectangle:
    """class for rectangle"""
    def __init__(self, width=0, height=0):
        """initialization necessary for objects, 3 parameters"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter for the width of rectangle"""
        # to retrieve it
        # private instance attribute width
        return self.__width

    @width.setter
    # property setter
    def width(self, width):
        #width must be an integer
        if isinstance(width, int) is False:
            # TypeError exception
            raise TypeError('width must be an integer')
        # if width is less than 0, raise a ValueError exception
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        """getter for height of rectangle"""
        return self.__height

    @height.setter
    #property setter
    def height(self, height):
        """setter for height of rectangle"""
        # must be an integer
        if isinstance(height, int) is False:
            raise TypeError('height must be an integer')
        # if height is less than 0, raise a ValueError
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
