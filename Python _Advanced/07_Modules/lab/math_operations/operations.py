def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def power(n1, n2):
    return n1 ** n2


mapper = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
}


def calculation(expression):
    num1, sign, num2 = expression.split()

    n1 = float(num1)
    n2 = float(num2)

    return mapper[sign](n1, n2)
