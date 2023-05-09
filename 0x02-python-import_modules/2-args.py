#!/usr/bin/python3
def main():
    """main - prints the number of and the list of its arguments"""

    from sys import argv

    le = len(argv)
    print(f"{le - 1} arguments:")

    for i in range(1, le):
        print(f"{i}: {argv[i]}")


if __name__ == "__main__":
    main()
