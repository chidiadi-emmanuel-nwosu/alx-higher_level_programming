#!/usr/bin/bash
def best_score(a_dictionary):
    if not len(a_dictionary.values()):
        return None
    return sorted(a_dictionary.items(), key=lambda x: x[1], reverse=True)[0][0]
