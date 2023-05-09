#!/usr/bin/python3
def main():
    """main - program entry point"""

    import calculator_1 as calc
    a = 10
    b = 5

    print(f"{a} + {b} = {calc.add(a, b)}")
    print(f"{a} - {b} = {calc.sub(a, b)}")
    print(f"{a} * {b} = {calc.mul(a, b)}")
    print(f"{a} / {b} = {calc.div(a, b)}")


if __name__ == "__main__":
    main()