#!/usr/bin/python3
def uppercase(str):
    """uppercase - prints a string in uppercase followed by a new line

    Args:
        str: input string

    Returns:
        None
    """
    str_len = len(str)
    for i in range(str_len):
        if i == str_len - 1:
            print("{}".format(chr(ord(str[i]) - 32)
                  if (ord(str[i]) >= 97 and ord(str[i]) <= 122) else (str[i])))
        else:
            print("{}".format(chr(ord(str[i]) - 32)
                  if (ord(str[i]) >= 97 and ord(str[i]) <= 122)
                      else (str[i])), end="")
