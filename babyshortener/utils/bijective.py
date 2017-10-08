# ----------------------------------------------------------------------------------------------------------------------

alphabet = 'V15mSgH3b8XyvTqWfCpknRzGxBJZYKNFd4atM7P9cQAr2sD6-hj_0Lw'
offset = 3024
base = len(alphabet)

# ----------------------------------------------------------------------------------------------------------------------


def encode(number):
    number += offset
    string = ''
    while number:
        string = alphabet[number % base] + string
        number //= base
    return string

# ----------------------------------------------------------------------------------------------------------------------


def decode(string):
    number = 0
    for char in string:
        number = number * base + alphabet.index(char)
    return number - offset

# ----------------------------------------------------------------------------------------------------------------------
