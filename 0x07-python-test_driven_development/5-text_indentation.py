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
        for index, char in enumerate(text):
            if char in chars:
                print(char)
                print()
            else:
                if text[index + 1] == "":
                    continue
                print(char, end='')
