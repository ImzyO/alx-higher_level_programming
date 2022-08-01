#!/usr/bin/python3
"""module for base.py"""
"""import module json, imports loads and dumps"""
import json

class Base:
    """a class named Base"""
    __nb_objects = 0
    """private class attribute"""
    def __init__(self, id=None):
        """initializes class Base"""
        #loop statement
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSOn string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return loads(list_dictionaries)
        
    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file:"""
        if list_objs is None:
            return []
        else: 
            for i in list_objs:
                list_objs = [i.to_dictionary()]
            with open("{}.json".format(type(cls).__name__), "w", encoding="utf-8") as f):
                f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string:"""
        if json_string is None:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set:"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances:"""
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]
