#!/usr/bin/python3
def main():
    """main - prints the number of and the list of its arguments"""

    from sys import argv

    _len = len(argv)
    le = _len - 1
    print("{} {}:".format(le, arguments if le != 1 else argument))

    for i in range(1, _len):
        print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
