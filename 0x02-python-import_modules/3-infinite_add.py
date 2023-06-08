#!/usr/bin/python3

if __name__ == "__main__":
    """ Program that prints the result of the addition of all arguments """

    import sys

    av = sys.argv[1:]
    ac = len(av)
    sums = 0

    for i in range(0, ac):
        sums += int(av[i])
    print("{:d}".format(sums))
