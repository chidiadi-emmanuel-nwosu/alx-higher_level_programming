#!/usr/bin/python3
"""1-write_file module
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)

    Args:
        filename: name of the file to be written to
        text: text string to be written to filename

    Returns:
        number of characters written to filename
    """

    with open(filename, 'w', encoding="utf-8") as file:
        return (file.write(text))
