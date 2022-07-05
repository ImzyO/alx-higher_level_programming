                                                             0x07. Python - Test-driven development
                                                             
                                                             https://docs.python.org/3.4/library/doctest.html
                                                             https://pymotw.com/3/doctest/
                                                             https://www.youtube.com/watch?v=1Lfv5tUGsn8
                                                             
REQUIREMENTS:
(a) Python Test cases
You are not allowed to import any modules in files 0 to 6
All your test files should be inside a folder tests
All your test files should be text files (extension: .txt)
All your tests should be executed by using this command: python3 -m doctest ./tests/*
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
We strongly encourage you to work together on test cases, so that you don’t miss any edge case – The Checker is checking for tests!

(b) Python Scripts
Your code should use the pycodestyle (version 2.8.*)
The first line of all your files should be exactly #!/usr/bin/python3


File 0: a function that adds 2 integers.    
        
File 2: a function that divides all elements of a matrix.
      
File 3: a function that prints My name is <first name> <last name>
        
File 4: a function that prints a square with the character #.
        
File 5: a function that prints a text with 2 new lines after each of these characters: ., ? and :
        There should be no space at the beginning or at the end of each printed line
        
File 6: Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.
        In this file, you will write unittests for the function def max_integer(list=[]):.
        Your test file should be inside a folder tests
        You have to use the unittest module - https://docs.python.org/3.4/library/unittest.html#module-unittest
        Your test file should be python files (extension: .py)
        Your test file should be executed by using this command: python3 -m unittest tests.6-max_integer_test
        All tests you make must be passable by the function below
        We strongly encourage you to work together on test cases, so that you don’t miss any edge case
