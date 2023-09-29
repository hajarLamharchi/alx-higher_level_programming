#!/usr/bin/python3
"""Time for interview documentation"""
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'

    r = requests.get(url)
    data = r.json()
    count = 0
    for k in data:
        count = count + 1
        if count == 11:
            break
        print('{}: {}'.format(k.get('sha'),
                              k.get('commit').get('author').get('name')))
