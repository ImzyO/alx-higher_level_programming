                                                      0x09. Python - Everything is object
                                                      
                               objects and values:     http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values
                                         aliasing:     http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing
                       immutable vs mutable types:     http://composingprograms.com/pages/24-mutable-data.html#sequence-objects
                                         mutation:     http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#cloning-lists
                                    cloning lists:     http://radar.oreilly.com/2014/10/python-tuples-immutable-but-potentially-changing.html
                                                      
 Reequirements: 
               .txt Answer Files - Only one line/ No Shebang/ All your files should end with a new line
               The first line of all your files should be exactly #!/usr/bin/python3
               All your files must be executable
 
 File 0: What function would you use to print the type of an object?
 
 File 1: What function would you use to print the type of an object?
 
 File 2: In the following code, do a and b point to the same object? Answer with Yes or No. 
 
                                                                                            >>> a = 89
                                                                                            >>> b = 100                                                               
                                                                                            
 File 3: In the following code, do a and b point to the same object? Answer with Yes or No.
 
                                                                                            >>> a = 89                                                                 
                                                                                            >>> b = 89
 
 File 4: In the following code, do a and b point to the same object? Answer with Yes or No. 
 
                                                                                            >>> a = 89
                                                                                            >>> b = a
 
 File 5: In the following code, do a and b point to the same object? Answer with Yes or No. 
 
                                                                                            >>> a = 89
                                                                                            >>> b = a + 1
 
 File 6:  What do these 3 lines print?
 
                                       >>> s1 = "Best School"
                                       >>> s2 = s1
                                       >>> print(s1 == s2)
                                       
File 7: What do these 3 lines print?

                                     >>> s1 = "Best"
                                     >>> s2 = s1
                                     >>> print(s1 is s2)
                                     
File 8: What do these 3 lines print?

                                     >>> s1 = "Best School"
                                     >>> s2 = "Best School"
                                     >>> print(s1 == s2)
                                     
File 9: What do these 3 lines print? 

                                     >>> s1 = "Best School"
                                     >>> s2 = "Best School"
                                     >>> print(s1 is s2)
                                     
File 10: What do these 3 lines print?

                                      >>> l1 = [1, 2, 3]
                                      >>> l2 = [1, 2, 3] 
                                      >>> print(l1 == l2)
                                      
File 11: What do these 3 lines print? 

                                      >>> l1 = [1, 2, 3]
                                      >>> l2 = [1, 2, 3] 
                                      >>> print(l1 is l2)    
         
File 12: What do these 3 lines print? 

                                      >>> l1 = [1, 2, 3]
                                      >>> l2 = l1
                                      >>> print(l1 == l2)
         
File 13: What do these 3 lines print? 

                                      >>> l1 = [1, 2, 3]
                                      >>> l2 = l1
                                      >>> print(l1 is l2)
         
File 14: What does this script print?

                                      l1 = [1, 2, 3]
                                      l2 = l1
                                      l1.append(4)
                                      print(l2)
                                      
File 15: What does this script print? 

                                      l1 = [1, 2, 3]
                                      l2 = l1
                                      l1 = l1 + [4]
                                      print(l2)

file 16: What does this script print? def increment(n):  
                                      n += 1
                                      
                                      a = 1
                                      increment(a)
                                      print(a)

file 17: What does this script print? def increment(n):
                                      n.append(4)
                                      
                                      l = [1, 2, 3]
                                      increment(l)
                                      print(l)
                                      
file 18: What does this script print? def assign_value(n, v):
                                      n = v
                                      
                                      l1 = [1, 2, 3]
                                      l2 = [4, 5, 6]
                                      assign_value(l1, l2)
                                      print(l1) 
                                      
File 19:  

          a function def copy_list(l): that returns a copy of a list.
          The input list can contain any type of objects
          Your file should be maximum 3-line long (no documentation needed)
          You are not allowed to import any module
          
File 20: 

         a = ()
         Is a a tuple? Answer with Yes or No.
         
File 21: 

         a = (1, 2)
         Is a a tuple? Answer with Yes or No.
         
File 22: 

         a = (1)
         Is a a tuple? Answer with Yes or No.
         
File 23: 

         a = (1, )
         Is a a tuple? Answer with Yes or No. 
         
File 24: What does this script print?  

                                       a = (1)
                                       b = (1)
                                       a is b
   
File 25: What does this script print? 

                                      a = (1, 2)
                                      b = (1, 2)
                                      a is b
                                      
file 26: What does this script print?

                                      a = ()
                                      b = ()
                                      a is b
                                      
file 27: Will the last line of this script print 139926795932424? Answer with Yes or No.  

                                                                                          >>> id(a)
                                                                                          139926795932424
                                                                                          >>> a
                                                                                          [1, 2, 3, 4]
                                                                                          >> a = a + [5]
                                                                                          >>> id(a) 
                                                                                          
file 28: Will the last line of this script print 139926795932424? Answer with Yes or No.  

                                                                                          >>> a
                                                                                          [1, 2, 3]
                                                                                          >>> id (a)
                                                                                          139926795932424
                                                                                          >>> a += [4]
                                                                                          >>> id(a)      
                                                                                          
file 29: a function magic_string() that returns a string “BestSchool” n times the number of the iteration
         Your file should be maximum 4-line long (no documentation needed)
         
         You are not allowed to import any module
         
file 30: a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance            attribute is called first_name.

         not allowed to import any module
         
file 31:  Assuming we are using a CPython implementation of Python3 with default options/configuration:

          How many int objects are created by the execution of the first line of the script? (103-line1.txt)
          How many int objects are created by the execution of the second line of the script (103-line2.txt)
          a = 1
          b = 1
          
file 32:  Assuming we are using a CPython implementation of Python3 with default options/configuration:

          How many int objects are created by the execution of the first line of the script? (104-line1.txt)
          How many int objects are created by the execution of the second line of the script (104-line2.txt)
          After the execution of line 3, is the int object pointed by a deleted? Answer with Yes or No (104-line3.txt)
          After the execution of line 4, is the int object pointed by b deleted? Answer with Yes or No (104-line4.txt)
          How many int objects are created by the execution of the last line of the script (104-line5.txt)
          a = 1024
          b = 1024
          del a
          del b
          c = 1024
          
file 33:  Assuming we are using a CPython implementation of Python3 with default options/configuration:

          Before the execution of line 2 (print("Love")), how many int objects have been created and are still in memory? (105-line1.txt)
          Why? (optional blog post :))
          Hint: NSMALLPOSINTS, NSMALLNEGINTS
          print("I")
          print("Love")
          print("Python")
          
file 34:  Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the               word):

          How many string objects are created by the execution of the first line of the script? (106-line1.txt)
          How many string objects are created by the execution of the second line of the script (106-line2.txt)
          After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No (106-line3.txt)
          After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No (106-line4.txt)
          How many string objects are created by the execution of the last line of the script (106-line5.txt)          
