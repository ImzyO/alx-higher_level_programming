#!/usr/bin/python3
"""module for load, add, save"""

from sys import argv
from os import path

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

Files_name = 'add_item.json'

if path.isfile(filename):
    new = load_from_json_file(Files_name)
else:
    new = []
for i in range(1, len(argv)):
    new.append(argv[i])
    save_to_json_file(new, Files_name)
