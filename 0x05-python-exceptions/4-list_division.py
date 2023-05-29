#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            ret = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            ret = 0
        except TypeError:
            print("wrong type")
            ret = 0
        except IndexError:
            print("out of range")
            return new_list
        finally:
            new_list.append(ret)
    return new_list
