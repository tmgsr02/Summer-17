def merge(lst1, lst2):
    """Merges two sorted lists recursively.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    combo = lst1 + lst2
    if len(combo) == 0: 
        return []
    else: 
        min_val = min(combo)
        if min_val in lst1: lst1.remove(min_val)
        if min_val in lst2: lst2.remove(min_val)
        return [min_val] + merge(lst1, lst2)

     
