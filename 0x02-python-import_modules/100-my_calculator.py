#!/usr/bin/python3
def main():
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    valid_op = {"+": add, "-": sub, "*": sub, "/": div}
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    if op not in list(valid_op.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, op, b, valid_op[op](a, b)))


if __name__ == "__main__":
    main()
