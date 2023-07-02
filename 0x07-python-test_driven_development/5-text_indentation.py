"""
Module contains one function: text_indentation

Prototype: def text_indentation(text)

Usage: text_indentation(text)
"""


def text_indentation(text):
    """
    Function use to print text base on the format

    Args:
        text(str): string use as arguments
    Raises:
        TypeError: if text is not a string
    """
    if not text or not isinstance(text, str):
        raise TypeError("text must be a string")
    chars = ['.', '?', ':']
    if len(text) != 0:
        test = 0
        for c in text:
            if test == 0 and c == ' ':
                continue
            elif test == 0 and c != ' ':
                test = 1

            if test == 1 and c in chars:
                print(c)
                print()
                test = 0
            elif test == 1:
                print(c, end="")
