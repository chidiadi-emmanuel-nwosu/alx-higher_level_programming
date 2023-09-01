#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password) and
   uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    param = {'per_page': 10, 'sort': 'committer-date', 'order': 'desc'}

    response = requests.get(url, params=param).json()

    for res in response:
        print(f"{res.get('sha')}: {res.get('commit').get('author').get('name')}")
