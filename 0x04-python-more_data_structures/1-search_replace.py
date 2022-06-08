#!/usr/python3
def search_replace(my_list, search, replace):
     new_list = []
     i = 1
     for h in my_list:
         if i== search:
              new_list.insert(search, replace)
         else:
               new_list.append(h)
               i += 1
     return new_list
