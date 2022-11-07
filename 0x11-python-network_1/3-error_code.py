#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8)."""
from urllib import request, error
from sys import argv
from urllib.error import HTTPError

if __name == '__main__':

    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            page = response.read()
            print(page.decode("utf-8")
    except HTTPError as err:
                print("Error code: {}".format(err.code))
