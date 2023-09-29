#!/usr/bin/python3
"""send a Post request and display the body of the response"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = ('email=' + email).encode('utf8')

    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf8')
    print(html)
