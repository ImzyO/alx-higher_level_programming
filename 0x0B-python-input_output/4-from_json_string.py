#!/usr/bin/python3
"""module for From JSONstring to Object"""

import json
#json module imported

def from_json_string(my_str):
    """
    a function that returns an object (Python data structure) 
    represented by a JSON string:
    """
    return json.loads(my_str)
