from math import pi

def pi_fraction(gap):
    """Print the fraction within gap of pi that has the smallest denominator.

    >>> pi_fraction(0.01)
    22 / 7 = 3.142857142857143
    >>> pi_fraction(1)
    3 / 1 = 3.0
    >>> pi_fraction(1/8)
    13 / 4 = 3.25
    >>> pi_fraction(1e-6)
    355 / 113 = 3.1415929203539825


    """
    numerator, denominator = 3, 1
    lower_bound, upper_bound = pi - gap, pi + gap

    while not lower_bound  < numerator/denominator < upper_bound:
        numerator += 1
        if numerator/(denominator + 1)  > lower_bound:
            denominator += 1

    print(numerator, '/', denominator, '=', numerator/denominator)
