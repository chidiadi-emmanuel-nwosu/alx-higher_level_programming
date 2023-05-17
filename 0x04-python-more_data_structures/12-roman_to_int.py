#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_string = roman_string.upper()

    r_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_num = 0
    old = 0

    for i in reversed(roman_string):
        new = r_num[i]
        int_num += new if new >= old else -new
        old = new

    return int_num
