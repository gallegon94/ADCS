import sys


def converter(num, pow):
    if num < 0:
        raise BaseException("Cannot convert negative numbers")

    if pow < 0:
        raise BaseException("Negative numbers are not valid as base number")

    res = ""
    while num != 0:
        residue = num % pow
        char = ''
        if residue >= 0 and residue <= 9:
            char = str(residue)
        else:
            char = chr(ord('A') + residue - 10)
        res = char + res
        num = num // pow
    return res

    number = sys.argv[1]
    try:
        number = int(number)
    except (Exception(e)):
        print("Not a number")
        sys.exit(1)
    print(converter(number, 16))
    print(converter(number, 2))
