#!/usr/bin/python3
"""append module
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after
       each line containing a specific string
    """
    with open(filename, 'r+', encoding="utf-8") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
        file.truncate()
