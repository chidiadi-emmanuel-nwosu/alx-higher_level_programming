#!/usr/bin/python3
def weight_average(my_list=[]):
    if not len(my_list):
        return 0

    num = sum(list(map(lambda x: x[0] * x[1], my_list)))
    div = sum(list(map(lambda x: x[1], my_list)))

    return num / div
