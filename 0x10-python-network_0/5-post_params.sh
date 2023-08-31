#!/bin/bash
# script that takes in a URL as an argument, sends a GET request to the URL,and displays the body of the response
curl -X POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" -s "$1"
