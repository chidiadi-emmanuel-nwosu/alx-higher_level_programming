#!/usr/bin/python3
def main():
    """main- prints all names defined in a module"""
    import hidden_4

    for name in dir(hidden_4):
        if name[0] == '_' and name[1] == '_':
            continue
        print(name)


if __name__ == "__main__":
    main()
