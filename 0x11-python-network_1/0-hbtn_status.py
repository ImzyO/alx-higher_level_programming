#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request as request

if __name__ == '__main__':

    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        res = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(res)))
        print("\t- content: {}".format(res))
        print("\t- utf8 content: {}".format(res.decode("utf-8")))
