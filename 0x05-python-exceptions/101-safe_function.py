#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(str(e)), file=stderr)
        return None
