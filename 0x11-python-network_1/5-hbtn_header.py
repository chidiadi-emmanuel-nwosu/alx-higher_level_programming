#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
   displays the value of the variable X-Request-Id in the response header
"""
import requests
import sys


response = requests.get(sys.argv[1])
data = response.headers.get('X-Request-Id')

print(data)
