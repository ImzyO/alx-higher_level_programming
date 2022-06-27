#!/usr/bin/python3
"""
module fo rectangle use only
"""

clas Rectangle:
    """
    class Rectangle that defines a rectangle by: (based on 2-rectangle.py
    """
    def __init__(self, width=0, height=0):
        """
        initialization
        """
        self.width = width
        self.height = height

        # method returns the string representation of the object
    
    def __str__(self):
        """
        string conversion
        """
        if self.__width == 0 or self.__height == 0:
            # return nothing, not area, not perimeter
            return ("")
        # print() and str() should print the rectangle with the character #
        string = (('#' * self.__width) + '\n') * self.__height
        return string[:-1]

    # Private instance attribute: width:
    @property
    def width(self):
        """
        getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for width
        """
        # width must be an integer
        if isinstance(value, int) is False:
            raise TypeError("must be an integer")

    if value < 0:
        raise ValueError("width must be >= 0")
    self.__width = value
    # private instance attribute: height:

    @property
    def height(self):
        """
        getter for height
        """
        return self.__height

    # property setter
    @height.setter
    def height(self, value):
        """
        height setter
        """
        if isinstance(value, int) is False:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    # Public instance method: def area(self):
    def area(self):
        """
        area of rectangle returned
        """
        return self.__height * self.__width

    # Public instance method
    def perimeter(self):
        """
        returns perimeter of rectangle
        """
        # with or height is equal to 0, perimeter has to be equal to 0
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
