#!/usr/bin/python3
"""displays the value of the variable X-Request-Id"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    header_dict = dict(r.headers)
    for k, v in header_dict.items():
        if k == 'X-Request-Id':
            print(v)
