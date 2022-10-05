#!/usr/bin/python3
"""module for anything squares"""
"""imports class Rectangle from module rectangle.py in the file models"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """a square class inherits from class rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes slass Square"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)
    
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        """returns formatted information display"""
        return '[{}] ({}) {}/{} - {}'.\
                format(type(self).__name__, self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """updates class Square, adds this public method"""
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for j, k in kwargs.items():
                if j == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = k
                elif j == "size":
                    self.size = k
                elif j == "x":
                    self.x = k
                elif j == "y":
                    self.y = k

    def to_dictionary(self):
        """method returns dictionary representation"""
        return {'id': self.id, 'x': self.x, 'y': self.y, 'size': self.width}
