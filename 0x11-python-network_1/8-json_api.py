#!/usr/bin/python3
"""Search API documentation"""

import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    data = {'q': q}

    r = requests.post(url, data=data)
    if r.headers.get('content-type') == 'application/json':
        res = r.json()
        if res:
            print('[{}] {}'.format(res.get('id'), res.get('name')))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
