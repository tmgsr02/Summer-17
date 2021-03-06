# Q2
def make_buzzer(n):
    """ Returns a function that prints numbers in a specified
    range except those divisible by n.

    >>> i_hate_fives = make_buzzer(5)
    >>> i_hate_fives(10)
    Buzz!
    1
    2
    3
    4
    Buzz!
    6
    7
    8
    9
    """
    def get_range(x):
        divisors = [i for i in range(x) if i%n == 0]
        for c in range(x):
            if c in divisors:
                print('Buzz!')
            else:
                print(c)

    return get_range 
# Q4
def f1():
    """
    >>> f1()
    3
    """
f1 =  lambda: 3

def f2():
    """
    >>> f2()()
    3
    """
    return  lambda:3

def f3():
    """
    >>> f3()(3)
    3
    """
    return lambda x:x

def f4():
    """
    >>> f4()()(3)()
    3
    """
    return lambda: lambda x: lambda: x

# Q6
def sum(n):
    """Computes the sum of all integers between 1 and n, inclusive.
    Assume n is positive.

    >>> sum(1)
    1
    >>> sum(5)  # 1 + 2 + 3 + 4 + 5
    15
    """
    if n == 1:
        return 1
    else:
        return n + sum(n-1)

# Q7

def sum_every_other_number(n):
    """Return the sum of every other natural number 
    up to n, inclusive.

    >>> sum_every_other_number(8)
    20
    >>> sum_every_other_number(9)
    25
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return n + sum_every_other_number(n - 2)


def fibonacci(n):
    """Return the nth fibonacci number.
    
    >>> fibonacci(11)
    89
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Q8
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n) 
    if n == 1:
        return 1

    elif n % 2 == 0:
        return 1 + hailstone(n//2)
    else:
        return 1 + hailstone(n * 3 + 1)
    
