def isPalindrome(x):
    # Write the doctests:
    """
    This checks if a given positive integer is a palindrome or not.
    >>> isPalindrome(121)
    True
    >>> isPalindrome(344)
    False
    >>> isPalindrome(-121)
    Traceback (most recent call last):
    ValueError: x must be a positive integer
    >>> isPalindrome("hello")
    Traceback (most recent call last):
    TypeError: x must be an integer
    """
    # Write the functionality:
    if not isinstance(x, int):
        raise TypeError('x must be an integer')
    elif x < 0:
        raise ValueError('x must be a positive integer')
    else:
        num_str = str(x)
        return num_str == num_str[::-1]