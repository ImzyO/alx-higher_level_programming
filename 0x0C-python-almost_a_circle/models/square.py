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
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError;
            pass
        else:
            print()

    def to_dictionary(self):
        """method returns dictionary representation"""
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
