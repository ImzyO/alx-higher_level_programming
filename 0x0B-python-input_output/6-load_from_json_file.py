#!/usr/bin/python3
"""module for create object from JSON file"""

import json
#imports built-in module json

def load_from_json_file(filename):
    """a function that creates an Object from a “JSON file”:"""
    with open(filename, encoding='utf-8') as F:
        return json.loads(F.read())
