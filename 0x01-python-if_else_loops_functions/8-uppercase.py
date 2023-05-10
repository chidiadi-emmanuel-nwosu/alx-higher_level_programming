#!/usr/bin/python3
def uppercase(str):
    """uppercase - prints a string in uppercase followed by a new line

    Args:
        str: input string

    Returns:
        None
    """
    s_len = len(str)
    count = 0
    for i in str:
        tmp = 32 if ord(i) >= 97 and ord(i) < 123 else 0
        print("{:c}".format(ord(i) - tmp), end="")
    print("")
