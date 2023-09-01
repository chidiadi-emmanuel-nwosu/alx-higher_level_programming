#!/usr/bin/python3
"""script that takes in a letter and sends a POST request
   to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = "" if sys.argv == 1 else sys.argv[1]
    param = {'q': letter}

    response = requests.post(url, param)
    try:
        data = response.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")

    except Exception:
        print("Not a valid JSON")
