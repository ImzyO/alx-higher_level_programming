#!/usr/bin/python3
"""module for Save object to file"""

import json
#imports json in-built module

def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file,
    using a JSON representation:
    """
    with open(filename, 'w', encoding="utf-8") as F:
        F.write(json.dumps(my_obj))
