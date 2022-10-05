#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and displays the body of the response."""
import requests
from sys import

if __name__ == "__main__":
    try:
        res = requests.get(argv[1])
        res.raise_for_status()
        print(res.text)
    except:
         print("Error code: {}".format(res.status_code))