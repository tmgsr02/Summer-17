# import square, triple, identity, and increment from the local file
from one_arg_fn import * 

def repeated(f, n):
    """Return the function that computes the nth application of f.

    >>> add_three = repeated(increment, 3)
    >>> add_three(5)
    8
    >>> repeated(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    """
    """ def compound(x): # Using the compound() fn, the program works. 
        nonlocal n       # was trying to avoid "nonlocal" but it seem tedious
        if n == 1:
            return f(x)
        else:
            n -= 1
            return compound(f(x))
    """
    def compose(x):
        
        return f(x) 
    
        
    return compound
        
