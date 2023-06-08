#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and the list of its arguments."""

    import sys

    av = sys.argv[1:]
    args = len(av)
    suf = "s" if args > 1 else ""
    print("{:d} argument{}".format(args, suf))
    for i in range(0, args):
        print("{:d}: {}".format(i, av[i]))
