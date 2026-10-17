
def validate_inputs(a, b):
    if type(a) is not int or type(b) is not int:
        raise TypeError("Inputs must be integers")

    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")


def add(a, b):
    validate_inputs(a, b)
    return a + b


def subtract(a, b):
    validate_inputs(a, b)
    return a - b


def multiply(a, b):
    validate_inputs(a, b)
    return a * b
