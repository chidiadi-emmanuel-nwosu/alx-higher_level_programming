#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import requests


url = "https://alx-intranet.hbtn.io/status"
response = requests.get(url)
data = response.text

print("Body response:")
print("\t- type: ", type(data))
print("\t- content:", data)
