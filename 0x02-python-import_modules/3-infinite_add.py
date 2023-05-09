#!/usr/bin/python3
def main():
    from sys import argv
    total = 0

    for arg in range(1, len(argv)):
        total += int(argv[arg])
    print(total)


if __name__ == "__main__":
    main()
