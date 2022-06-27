#!/usr/bin/python3
"""
square module - prints square
"""
class Square:
    """
    square class with fiunction to print square
    """
    def __init__(self, size=0):
        """
        intitialization for square, takes in int size
        """
        self.__check_size__(size)
        self.__size = size

    @property
    #property define size(self) to retrieve it
    def size(self):
        """
        size getter, returns the private size
        """
        return (self.__size)

    @size.setter
    #propertysetter def size(self, value) to set it
    def size(self, value):
        """
        size setter, sets the private setter
        """
        self.__check_size__(value)
        self.__size = value

    #public instance method
    def area(self):
        """
        returns area of the square
        """
        return (self.__size ** 2)

    #public instance method, could do it with join as well
    def my_print(self):
        """
        Prints the square! should only print a newline if size is 0
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    if j == (self.size - 1):
                        print("#")
                        break
                    print("#", end="")

    def __check_size__(self, size):
        """
        size error chechking
        """
        #size must be an integer, otherwise raise TypeError exception
        if type(size) != int:
            raise TypeError("size must be an integer")
            #if size is less than 0, raise valueerror
        if size < 0:
            raise ValueError("size must be >= 0")
