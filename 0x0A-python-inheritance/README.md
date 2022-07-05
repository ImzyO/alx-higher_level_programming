                                                                  0x0A. Python - Inheritance
                                                                  
                                                                  https://docs.python.org/3/tutorial/classes.html#inheritance
                                                                  https://docs.python.org/3/tutorial/classes.html#multiple-inheritance
                                                                  https://www.packt.com/inheritance-python/
                                                                  https://www.youtube.com/watch?v=d8kCdLCi6Lk
                                                                  
REQUIREMENTS: 
Python Test Cases: 

                        All your test files should be inside a folder tests
                        All your test files should be text files (extension: .txt)
                        All your tests should be executed by using this command: python3 -m doctest ./tests/*
                        All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
                        All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
                        All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'                           and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
                        A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will                         be verified)

Documentation
                       Do not use the works import or from inside your comments, the checker will think you try to import some modules
                       
NB: /No modules have been imported in all files/                       



file 0: a function that returns the list of available attributes and methods of an object:

file 1:  a class MyList that inherits from list:

file 2: a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

file 3: a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise             False.

file 4:  a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

file 5: an empty class BaseGeometry.

file 6: a class BaseGeometry (based on 5-base_geometry.py).

file 7: a class BaseGeometry (based on 6-base_geometry.py).

file 8: a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

file 9: a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)

file 10: a class Square that inherits from Rectangle (9-rectangle.py):

file 11: a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).
