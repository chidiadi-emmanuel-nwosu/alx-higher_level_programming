#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """search_replace - replaces all occurrences of an
                        element by another in a new list.
    Args:
        my_list: the initial list
        search: the element to replace in the list
        replace: the new element

    Returns:
        new list with the replaced value
    """
    return list(map(lambda x: replace if x == search else x, my_list))
