# add two number.

def add2num(x, y):
    '''Add two numbers and return sum.
    >>> add2num(3, 5)
    8
    >>> add2num(-10.5, 8)
    -2.5
    >>> add2num(8, 'hello')
    Traceback (most recent call last):
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    '''

    return x + y

def mul(x, y):
    """Multiplies two given numbers and returns the product.
    >>> mul(6, 7)
    42
    >>> mul(-8, 7)
    >>> -56
    """
    return x * y