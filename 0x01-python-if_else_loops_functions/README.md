0x01. Python - if/else, loops, functions

Python programming    NB:(prefix numbers based on file...)

File 0: A programm that assigns a random signed number to the variable number each time it is executed completes the source code in order to print whether the number             stored in the variable number is positive or negative.
        
File 1: A programm assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number         stored in the variable number

File 2: A program that prints the ASCII alphabet, in lowercase, not followed by a new line.

File 3: A program that prints the ASCII alphabet, in lowercase, not followed by a new line, Prints all the letters except q and e

File 4: A program that prints all numbers from 0 to 98 in decimal and in hexadecimal

File 5: A program that prints numbers from 0 to 99,  printed in ascending order, with two digits

File 6: A program that prints all possible different combinations of two digits
        The two digits must be different
        01 and 10 are considered the same combination of the two digits 0 and 1
        Prints only the smallest combination of two digits

File 7: A function that checks for lowercase character
        You are not allowed to use str.upper() and str.isupper()
        
File 8: A function that prints a string in uppercase followed by a new line
        You are not allowed to use str.upper() and str.isupper()
        
File 9: A function that prints the last digit of a number
        Returns the value of the last digit
        
File 10:  A function that adds two integers and returns the result
          Returns the value of a + b
          
File 11: A function that computes a to the power of b and return the value
          Returns the value of a ^ b
          
File 12: A function that prints the numbers from 1 to 100 separated by a space

File 100: A program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase)

File 101: A function that creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”)

File 102: Writes the Python function def magic_calculation(a, b, c): that does exactly the same as the following Python bytecode:

          3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
