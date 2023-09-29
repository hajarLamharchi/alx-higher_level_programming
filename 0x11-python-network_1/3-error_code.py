#!/usr/bin/python3
"""This script displays the body of the responese"""

import urllib.error
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as r:
            html = r.read()
        print(html.decode('utf8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.status))
