def zero(m=None):
    if m is not None:
        if m[0] == "+":
            return 0 + m[-1]
        elif m[0] == "-":
            return 0 - m[-1]
        elif m[0] == "*":
            return 0 * m[-1]
        else:
            return 0 // m[-1]
    else:
        return 0

def one(m=None):
    if m is not None:
        if m[0] == "+":
            return 1 + m[-1]
        elif m[0] == "-":
            return 1 - m[-1]
        elif m[0] == "*":
            return 1 * m[-1]
        else:
            return 1 // m[-1]
    else:
        return 1

def two(m=None):
    if m is not None:
        if m[0] == "+":
            return 2 + m[-1]
        elif m[0] == "-":
            return 2 - m[-1]
        elif m[0] == "*":
            return 2 * m[-1]
        else:
            return 2 // m[-1]
    else:
        return 2

def three(m=None):
    if m is not None:
        if m[0] == "+":
            return 3 + m[-1]
        elif m[0] == "-":
            return 3 - m[-1]
        elif m[0] == "*":
            return 3 * m[-1]
        else:
            return 3 // m[-1]
    else:
        return 3

def four(m=None):
    if m is not None:
        if m[0] == "+":
            return 4 + m[-1]
        elif m[0] == "-":
            return 4 - m[-1]
        elif m[0] == "*":
            return 4 * m[-1]
        else:
            return 4 // m[-1]
    else:
        return 4

def five(m=None):
    if m is not None:
        if m[0] == "+":
            return 5 + m[-1]
        elif m[0] == "-":
            return 5 - m[-1]
        elif m[0] == "*":
            return 5 * m[-1]
        else:
            return 5 // m[-1]
    else:
        return 5

def six(m=None):
    if m is not None:
        if m[0] == "+":
            return 6 + m[-1]
        elif m[0] == "-":
            return 6 - m[-1]
        elif m[0] == "*":
            return 6 * m[-1]
        else:
            return 6 // m[-1]
    else:
        return 6

def seven(m=None):
    if m is not None:
        if m[0] == "+":
            return 7 + m[-1]
        elif m[0] == "-":
            return 7 - m[-1]
        elif m[0] == "*":
            return 7 * m[-1]
        else:
            return 7 // m[-1]
    else:
        return 7

def eight(m=None):
    if m is not None:
        if m[0] == "+":
            return 8 + m[-1]
        elif m[0] == "-":
            return 8 - m[-1]
        elif m[0] == "*":
            return 8 * m[-1]
        else:
            return 8 // m[-1]
    else:
        return 8

def nine(m=None):
    if m is not None:
        if m[0] == "+":
            return 9 + m[-1]
        elif m[0] == "-":
            return 9 - m[-1]
        elif m[0] == "*":
            return 9 * m[-1]
        else:
            return 9 // m[-1]
    else:
        return 9

def plus(n):
    return "+", n
def minus(n):
    return "-", n
def times(n):
    return "*", n
def divided_by(n):
    return "//", n


print(six(divided_by(two())))