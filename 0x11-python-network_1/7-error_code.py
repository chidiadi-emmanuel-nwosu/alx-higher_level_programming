#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
   displays the body of the response.
"""
import requests
import sys


response = requests.get(sys.argv[1])
if response.status_code == 200:
    print(response.text)
else:
    print("Error code: ", response.status_code)
