def get_seven_c(x):
    """
    >>> x = [1, [2, [3, [4, [5, [6, [7]]]]]]]
    >>> get_seven_c(x)
    7
    """
    #while len(x) == 2:
    #    x = x[1]
       
            
    return x[1][1][1][1][1][1][0]
