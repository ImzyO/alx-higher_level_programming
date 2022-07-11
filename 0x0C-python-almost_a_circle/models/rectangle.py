#!/usr/bin/python3
"""module for First rectangle"""
from models.base import Base
"""module base in models file contains class Base which is imported"""

class Rectangle(Base):
    """a class called rectangle that inherits from class Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes class Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        self.__width

    @width.setter
    def width(self, width):
        try:
            type(width) == int
            width > 0
        except TypeError:
            raise TypeError("width value must be an integer")
        else ValueError:
            raise ValueError("width value must be > 0")
        self.__width = width

    @property
    def height(self):
        self.__height

    @height.setter(self, height):
        try:
            type(height) == int
            height > 0

        except TypeError:
            raise TypeError("height must be an integer")
        else ValueError:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        self.__x

    @x.setter
    def x(self, x):
        try:
            type(x) == int
            x > 0
        except TypeError:
            raise TypeError("x must be an integer")
        else ValueError:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        self.__y

    @y.setter
    def y(self, y):
        try:
            type(y) == int
            y > 0
        except TypeError:
            raise TypeError("y must be an integer")
        else ValueError:
            raise ValueError("y must be >= 0")

    def area(self):
        """public method returns area of rectangle"""
        return self.width * self.height

    def display(self):
        """public method printgs to stdout the rectangle instance with '#'"""
        if self.__y != 0:
            for newline in range(self.__y):
                print()
        for row in range(self.__height):
            print((self.__x * " ") + (self.__width * '#'))

    def __str__(self):
        """method returns formatted display information"""
        return '[{}] ({}) {}/{} - {}/{}'.\
                format(type(self).__name__, self.id, self.x, self.y, self.width,self.height)
