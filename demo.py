def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def compound_method(a, b):
    if a > b:
        return add(a, b) + multiply(a, b)
    return add(a, b) * multiply(a, b)
