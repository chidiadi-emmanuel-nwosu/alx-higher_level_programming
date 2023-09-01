#!/usr/bin/python3
"""script that takes in a letter and sends a POST request
   to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


url = "http://0.0.0.0:5000/search_user"
try:
    param = {'q': sys.argv[1]}
except Exception:
    param = {'q': ""}

response = requests.post(url, param)
try:
    data = response.json()
except Exception as e:
    print("Not a valid JSON")

if data:
    print(f"[{data['id']}] {data['name']}")
else:
    print("No result")
