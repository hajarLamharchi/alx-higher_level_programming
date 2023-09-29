#!/usr/bin/python3
"""This script displays the id of your github account"""

import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = f'https://api.github.com/users/{username}'

    headers = {'Authorization': f'Bearer {token}',
               'X-GitHub-Api-Version': '2022-11-28',
               'Accept': 'application/vnd.github.v3+json',
               }
    r = requests.get(url, headers=headers)
    data = r.json()
    print(data.get('id'))
