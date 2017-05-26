def choose(n, k):
    """Returns the number of ways to choose K items from
    N items.
    >>> choose(5, 2)
    10
    >>> choose(20, 6)
    38760
    """
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    return int(factorial(n)/(factorial(k) * factorial(n-k)))
