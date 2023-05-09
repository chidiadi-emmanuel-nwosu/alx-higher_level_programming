#!/usr/bin/python3
def print_last_digit(number):
    """print_last_digit - prints the last digit of a number

    Args:
        number: number input

    Returns:
        the value of the last digit
    """

    if number < 0:
        number = -number
    last = number % 10
    print(last, end="")
    return last
