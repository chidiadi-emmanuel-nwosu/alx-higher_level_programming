#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password) and
   uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    token = sys.argv[2]
    url = 'https://api.github.com/user'

    response = requests.get(url, auth=requests.auth.HTTPBasicAuth(user, token))
    print(response.json().get('id'))
