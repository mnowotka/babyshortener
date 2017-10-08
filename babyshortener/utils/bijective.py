"""This file defines a bijective function that converts database primary key (integer) into string and the other way
around. In this case the function is basically baseN, where N = 62 (a-z,A-Z,0-9) with following modifications:

- alphabet is shuffled
- there is an offset added so the result can't be shorter than 3 characters

"""

# ----------------------------------------------------------------------------------------------------------------------

# shuffled letters to make it more random for small ID values
alphabet = 'PfAwbxBOScL1ajEqsNuVJH7QhCmiK2y80vR39UpTzWMlXn46edIGgFZYDokrt5'
base = len(alphabet)

# adding offset so the result has at least 3 characters
offset = (base ** 2) - 1

# ----------------------------------------------------------------------------------------------------------------------


def encode(number):
    """
    
    Straightforward implementation of baseN encoding with the offset twist
    """
    number += offset
    string = ''
    while number:
        string = alphabet[number % base] + string
        number //= base
    return string

# ----------------------------------------------------------------------------------------------------------------------


def decode(string):
    """

    Straightforward implementation of baseN decoding with the offset twist
    """
    number = 0
    for char in string:
        number = number * base + alphabet.index(char)
    return number - offset

# ----------------------------------------------------------------------------------------------------------------------
