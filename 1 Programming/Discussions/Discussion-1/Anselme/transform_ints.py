def transform_ints(func, n):
    """Print out all integers from 1 to n with func applied
    on them.
    >>> def square(x):
    ...     return x * x
    >>> transform_ints(square, 3)
    1
    4
    9
    """
    for v in range(1,n+1):
        print(func(v))
    return 
