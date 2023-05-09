#!/usr/bin/python3
def remove_char_at(str, n):
    """remove_char_at - creates a copy of the string,
                        removing the character at the position n

    Args:
        str: input string
        n: position where the character is ignored

    Returns:
        copy of created string
    """

    copy = ""
    for i in range(len(str)):
        if i == n:
            pass
        else:
            copy += str[i]
    return copy
