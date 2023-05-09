#!/usr/bin/python3
def uppercase(str):
    """uppercase - prints a string in uppercase followed by a new line

    Args:
        str: input string

    Returns:
        None
    """
    for i in str:
        print("{:c}".format(ord(i) - 32 if (ord(i) >= 97
              and ord(i) <= 122) else ord(i)), end="")
    print()
