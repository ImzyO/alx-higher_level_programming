#!/usr/python3
def search_replace(my_list, search, replace):
    def element_replace_search(i):
         return (i if i != search else replace)
         return list(map(element_replace_search, my_list))
