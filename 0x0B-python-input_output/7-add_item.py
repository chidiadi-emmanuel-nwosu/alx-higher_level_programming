#!/usr/bin/python3
"""7-add_item
"""

import os
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.exists("add_item.json"):
    _list = load_from_json_file("add_item.json")
else:
    _list = []

for i in range(1, len(sys.argv)):
    _list.append(sys.argv[i])

save_to_json_file(_list, "add_item.json")
