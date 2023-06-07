#!/usr/bin/python3
"""Module to find and add characters
"""


def text_indentation(text):
    """prints a text with 2 new lines after
       each of these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    text = text.strip()
    res = ""
    check = 0

    for i in range(len(text)):
        if check == 0:
            res += text[i]
        if text[i] in ".?:":
            res += "\n\n"
            if text[i + 1] == " ":
                check = 1
        else:
            check = 0
    print(res, end="")
