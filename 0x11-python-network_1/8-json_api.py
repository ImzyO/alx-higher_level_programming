#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
from sys import argv
if __name__ == "__main__":
    letter = ''
    if len(argv) == 2:
        letters = argv[1]
    try:
        res = requests.post("http://0.0.0.0:5000/search_user", data={'q': letters}).json()
        if ("id" in res) and ("name" in res):
            print("[{}] {}".format(res['id'], res['name']))
        else:
            print("No result")
    except:
       print("Not a valid JSON") 
