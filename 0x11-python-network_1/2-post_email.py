#!/usr/bin/python3
"""script that takes in a URL and an email,
   sends a POST request to the passed URL with the email as a parameter,
   and displays the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    param = {'email': email}
    data = urllib.parse.urlencode(param).encode('utf-8')
    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as response:
        res = response.read()
        print(res)
