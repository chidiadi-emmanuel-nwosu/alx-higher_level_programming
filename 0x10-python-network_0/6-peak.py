#!/usr/bin/python3
"""find peak module"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""

    # get the length of the list
    length = len(list_of_integers)

    # check if it is an empty list
    if length == 0:
        return None

    # check if the list contains only one or only two integers
    if length <= 2:
        return max(list_of_integers)

    # get the mid point of the list
    mid = int(length / 2)

    # set the peak value to the integer at the midpoint
    peak = list_of_integers[mid]

    # check if the peak value satisfies the conditions
    if peak > list_of_integers[mid + 1] and peak > list_of_integers[mid + 1]:
        return peak

    # recursively check half of the list if the initial
    # peak value does not satisfy the conditions
    if peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid:])
