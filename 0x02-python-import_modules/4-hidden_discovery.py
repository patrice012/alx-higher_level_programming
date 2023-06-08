#!/usr/bin/python3

if __name__ == "__main__":
    """ Print name store in hidden.py file"""
    import hidden_4

    args = dir(hidden_4)
    for i in args:
        if i[:2] != "__":
            print(i)
