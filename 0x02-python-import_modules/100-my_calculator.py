#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    def result(a, operator, b):
        if operator == '+':
            return add(a, b)
        elif operator == '-':
            return sub(a, b)
        elif operator == '*':
            return mul(a, b)
        elif operator == '/':
            return div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    cal = result(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]))
    print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], cal))
