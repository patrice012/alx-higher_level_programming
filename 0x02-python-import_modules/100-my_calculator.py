#!/usr/bin/python3

if __name__ == "__main__":
    """Build my own calculator! """

    import sys
    from calculator_1 import add, sub, mul, div

    arg_array = sys.argv[1:]
    arg_count = len(arg_array)

    if arg_count != 3:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)
    else:
        operator = arg_array[1]
        a = int(arg_array[0])
        b = int(arg_array[2])

        match operator:
            case "+":
                print("{:d} {:d} {} = {}".format(a, b, operator, add(a, b)))
                exit(0)
            case "-":
                print("{:d} {:d} {} = {}".format(a, b, operator, sub(a, b)))
                exit(0)
            case "*":
                print("{:d} {:d} {} = {}".format(a, b, operator, mul(a, b)))
                exit(1)
            case "/":
                print("{:d} {:d} {} = {}".format(a, b, operator, div(a, b)))
                exit(1)
            case _:
                print("Unknown operator. Available operators: +, -, * and /")
                exit(1)
