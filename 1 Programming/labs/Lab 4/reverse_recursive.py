def reverse_recursive(lst):
    """Returns the reverse of the given list.

    >>> reverse_recursive([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    if len(lst) == 1: return lst
    else: return lst[-1:] + reverse_recursive(lst[0:-1])
   
     """i = []
    while len(lst) > 0:
        i.append(lst[-1])
        lst = lst[0:-1]
    return i
    """
