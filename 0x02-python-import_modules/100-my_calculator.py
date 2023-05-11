#!/usr/bin/python3
def main():
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    match op:
        case "+":
            print(f"{a} {op} {b} = {add(a, b)}")
        case "-":
            print(f"{a} {op} {b} = {sub(a, b)}")
        case "*":
            print(f"{a} {op} {b} = {mul(a, b)}")
        case "/":
            print(f"{a} {op} {b} = {div(a, b)}")
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)


if __name__ == "__main__":
    main()
