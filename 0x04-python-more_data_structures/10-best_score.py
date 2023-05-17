#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or not len(a_dictionary):
        return None
    max_value = max(a_dictionary.values())
    for i in a_dictionary.keys():
        if a_dictionary[i] == max_value:
            return i
