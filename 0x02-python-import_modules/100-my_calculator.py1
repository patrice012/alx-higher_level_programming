#!/usr/bin/python3

if __name__ == "__main__":
    """Build my own calculator! """

    import sys
    from calculator_1 import add, sub, mul, div

    arg_array = sys.argv[1:]
    arg_count = len(arg_array)

    if arg_count != 3:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    else:
        op = arg_array[1]
        a = int(arg_array[0])
        b = int(arg_array[2])

        match op:
            case "+":
                print("{:d} {} {:d} = {}".format(a, op, b, add(a, b)))
                sys.exit(0)
            case "-":
                print("{:d} {} {:d} = {}".format(a, op, b, sub(a, b)))
                sys.exit(0)
            case "*":
                print("{:d} {} {:d} = {}".format(a, op, b, mul(a, b)))
                sys.exit(0)
            case "/":
                print("{:d} {} {:d} = {}".format(a, op, b, div(a, b)))
                sys.exit(0)
            case _:
                print("Unknown operator. Available operators: +, -, * and /")
                sys.exit(1)
