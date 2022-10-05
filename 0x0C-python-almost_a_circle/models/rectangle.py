#!/usr/bin/python3
"""module for First rectangle"""
"""module base in models file contains class Base which is imported"""
from models.base import Base

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
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(vx) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """public method returns area of rectangle"""
        return self.width * self.height

    def display(self):
        """public method printgs to stdout the rectangle instance with '#'"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """method returns formatted display information"""
        return '[{}] ({}) {}/{} - {}/{}'.\
                format(type(self).__name__, self.id, self.x, self.y, self.width,self.height)

    def update(self, *args, **kwargs):
        """updates methods, values"""
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for j, k in kwargs.items():
                if j == "id":
                    if k is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = k
                elif j == "width":
                    self.width = k
                elif j == "height":
                    self.height = k
                elif j == "x":
                    self.x = k
                elif j == "y":
                    self.y = k

    def dictionary(self):
        """method returns dictionary represantation of this class"""
        return {"id": self.id, "width": self.__width, "height": self.__height, "x": self.__x, "y": self.__y}
