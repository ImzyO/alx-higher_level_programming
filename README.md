This project looks into Python programming                    NB: Prefixes are numbers

File 0: Shell script that runs a Python script.
        The Python file name will be saved in the environment variable $PYFILE
        
File 1: Shell script that runs Python code.
        The Python code will be saved in the environment variable $PYCODE
 
File 2: Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.
        Uses the function print
        
File 3: Completes the source code: 

                                   #!/usr/bin/python3
                                   number = 98                                                        
                                   # YOUR CODE GOES HERE. PLEASE REMOVE THIS                                  
        in order to print the integer stored in the variable called number, followed by Battery street, followed by a new line. uses f-strings
        
File 4: Completes the source code:

                                   #!/usr/bin/python3                                 
                                   number = 3.14159                                 
                                   # YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE                            
        in order to print the float stored in the variable number with a precision of 2 digits
        The output of the program should be:   Float:, followed by the float with only 2 digits followed by a new line. uses f-strings
        
File 5: Completes this source code: 

                                    #!/usr/bin/python3                                   
                                    str = "Holberton School"                                    
                                    # YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE                                   
       in order to print 3 times a string stored in the variable str, followed by its first 9 characters.
       
File 6: Completes this source code: 

                                    #!/usr/bin/python3                                    
                                    str1 = "Holberton"                                   
                                    str2 = "School"                                   
                                    # YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE                                   
                                    print(f"Welcome to {str1}!"                                 
        to print Welcome to Holberton School!
        
File 7: Completes this source code: 

                                    #!/usr/bin/python3                                    
                                    word = "Holberton"                                   
                                    # YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE                                    
                                    print(f"First 3 letters: {word_first_3}")                                    
                                    print(f"Last 2 letters: {word_last_2}")
                                    print(f"Middle word: {middle_word}")
                                    
File 8: Completes this source code: 
                                    #!/usr/bin/python3
                                    str = "Python is an interpreted, interactive, object-oriented programming\
                                    language that combines remarkable power with very clear syntax"
                                    # YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
                                    print(str)                          
        to print object-oriented programming with Python, followed by a new line.

File 9: Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.
        Script maximum: 98 characters long (please check with wc -m 9-easter_egg.py)
        
File 100: Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.
          Uses the function write from the sys module
          Script  prints to stderr
          Script exits with the status code 1
          
File 101: script that compiles a Python script file.
          The Python file name will be stored in the environment variable $PYFILE
          The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)
          
File 102: Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:

            3           0 LOAD_CONST                         1 (98)
                        3 LOAD_FAST                          0 (a)
                        6 LOAD_FAST                          1 (b)
                        9 BINARY_POWER
                        10 BINARY_ADD
                        11 RETURN_VALUE
