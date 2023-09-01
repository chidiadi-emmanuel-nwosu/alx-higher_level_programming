#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password) and
   uses the GitHub API to display your id
"""
import requests
import sys


user = sys.argv[1]
token = sys.argv[2]
url = f'https://api.github.com/{user}'
param = {'Authorization': f'token {token}'}

response = requests.get(url, headers=param)
try:
    data = response.json()
except Exception as e:
    print("Not a valid JSON")

if data:
    print(data)
else:
    print("No result")
