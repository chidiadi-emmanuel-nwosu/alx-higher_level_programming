#!/usr/bin/python3
"""2-append_write.py
"""


def append_write(filename="", text=""):
    """appends a string at the endof  a text file (UTF8)

    Args:
        filename: name of the file to be written to
        text: text string to append

    Returns:
        number of characters appended to filename
    """

    with open(filename, 'a', encoding="utf-8") as file:
        return (file.write(text))
