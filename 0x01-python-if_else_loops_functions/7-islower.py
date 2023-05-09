#!/usr/bin/pyhton3
def islower(c):
    """islower - checks if a character is lowercase

    Args:
        c: character input

    Returns:
        True if c is lowerecase
        False otherwise
    """

    if ord(c) >= 97 and ord(c) <= 122:
        return True
    return False
