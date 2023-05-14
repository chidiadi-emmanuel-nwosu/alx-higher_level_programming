#!/usr/bin/python3

# File: 8-multiple_returns.py
# Author: Chidiadi E Nwosu

def multiple_returns(sentence):
    """multiple_returns - returns a tuple with the length
                          of a string and its first character.
    Args:
        sentence: string input

    Returns:
        tuple with the length of sentence and its first character.
    """
    length = len(sentence)
    if length == 0:
        return length, None
    else:
        return length, sentence[0]
