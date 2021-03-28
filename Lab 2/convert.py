def int_to_str(number):
    if not isinstance(number, int):
        raise Exception("Not a number!")

    base = 10
    result = ""
    sign = ""
    if number < 0:
        sign = "-"
        number = number * -1  # Handle all numbers as positive

    if number == 0:
        return "0"

    while number != 0:
        result = chr(ord("0") + number % base) + result
        number = number // base

    return sign + result


def str_to_int(string):
    if not isinstance(string, str):
        raise Exception("Not a string!")

    if string == "":
        raise Exception("Empty string")
    base = 10
    pow = 1
    res = 0
    sign = 1

    if string[0] == "-" or string[0] == "+":
        if string[0] == "-":
            sign = -1
        string = string[1:]

    for char in string[::-1]:
        digit = (ord(char) - ord('0'))
        if digit < 0 or digit > 9:
            raise Exception("Not a number!")
        res = res + digit * pow
        pow = pow * base

    return sign * res
