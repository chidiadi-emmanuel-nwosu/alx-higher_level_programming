#!/usr/bin/python3
def uppercase(str):
    """uppercase - prints a string in uppercase followed by a new line

    Args:
        str: input string

    Returns:
        None
    """

    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            print(chr(ord(i) - 32), end="")
        else:
            print(i, end="")
    print()
