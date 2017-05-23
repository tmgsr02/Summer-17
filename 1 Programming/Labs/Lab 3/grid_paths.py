from fractions import Fraction
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    >>> paths(3, 3)
    6
    """
    if m == 1 or n == 1: 
        return int(Fraction(1, 1))
    else:
        return  int(Fraction(m+n-2, n-1) * paths(m, n-1))
    
    
