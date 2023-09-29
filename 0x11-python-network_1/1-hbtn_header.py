#!/usr/bin/python3
"""This script dispalys the value of the X-Request-Id variable"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as r:
        header_dict = dict(r.headers)
        for k, v in header_dict.items():
            if k == 'X-Request-Id':
                print(v)
