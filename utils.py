from sympy import symbols, Matrix, cos, sin, Symbol


def Tx(s):
    # assert type(s) == Symbol
    return Matrix(
        [[1, 0, 0, s],
         [0, 1, 0, 0],
         [0, 0, 1, 0],
         [0, 0, 0, 1]]
    )


def Ty(s):
    # assert type(s) == Symbol
    return Matrix(
        [[1, 0, 0, 0],
         [0, 1, 0, s],
         [0, 0, 1, 0],
         [0, 0, 0, 1]]
    )


def Tz(s):
    # assert type(s) == Symbol
    return Matrix(
        [[1, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 1, s],
         [0, 0, 0, 1]]
    )


def Txd():
    return Matrix(
        [[0, 0, 0, 1],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    )


def Tyd():
    return Matrix(
        [[0, 0, 0, 0],
         [0, 0, 0, 1],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    )


def Tzd():
    return Matrix(
        [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 1],
         [0, 0, 0, 0]]
    )


def Rx(q):
    # assert type(q) == Symbol
    return Matrix(
        [[1, 0, 0, 0],
         [0, cos(q), -sin(q), 0],
         [0, sin(q), cos(q), 0],
         [0, 0, 0, 1]]
    )


def Ry(q):
    # assert type(q) == Symbol
    return Matrix(
        [[cos(q), 0, sin(q), 0],
         [0, 1, 0, 0],
         [-sin(q), 0, cos(q), 0],
         [0, 0, 0, 1]]
    )


def Rz(q):
    # assert type(q) == Symbol
    return Matrix(
        [[cos(q), -sin(q), 0, 0],
         [sin(q), cos(q), 0, 0],
         [0, 0, 1, 0],
         [0, 0, 0, 1]]
    )


def Rxd(q):
    # assert type(q) == Symbol
    return Matrix(
        [[0, 0, 0, 0],
         [0, -sin(q), -cos(q), 0],
         [0, cos(q), -sin(q), 0],
         [0, 0, 0, 0]]
    )


def Ryd(q):
    # assert type(q) == Symbol
    return Matrix(
        [[-sin(q), 0, cos(q), 0],
         [0, 0, 0, 0],
         [-cos(q), 0, -sin(q), 0],
         [0, 0, 0, 0]]
    )


def Rzd(q):
    # assert type(q) == Symbol
    return Matrix(
        [[-sin(q), -cos(q), 0, 0],
         [cos(q), -sin(q), 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    )


def toSym(s):
    if "-" in s:
        return -symbols(s[1::])
    else:
        return symbols(s)
