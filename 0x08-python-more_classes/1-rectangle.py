#!/usr/bin/python
"""
module for only rectangle use
"""
class Rectangle:
    """class for rectangle"""
    def __init__(self, width=0, height=0):
        """initialization necessary for objects, 3 parameters"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the width of rectangle"""
        # to retrieve it
        # private instance attribute width
        return self.__width

    @width.setter
    # property setter
    def width(self, value):
        #width must be an integer
        if isinstance(value, int) is False:
            # TypeError exception
            raise TypeError('width must be an integer')
        # if width is less than 0, raise a ValueError exception
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """getter for height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """getter for heiight"""
        # Private instance attribute: height:
        return self.__height

    @height.setter
    #property setter
    def height(self, value):
        """setter for height of rectangle"""
        # must be an integer
        if isinstance(value, int) is False:
            raise TypeError('height must be an integer')
        # if height is less than 0, raise a ValueError
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
