#!/usr/bin/python3
if __name__ == "__main__":
    from 100-my_calculator import a operator b
    from sys import argv

    if argv != a operator b:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return 1

    operator = +, -, *, /

    if operator != operator:
        print("Unknown operator. Available operators: +, -, * and /")
        return 1
    else:
        print("<a> <operator> <b> = <result>")
