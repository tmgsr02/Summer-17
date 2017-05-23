from merge import merge
def mergesort(seq):
    """Mergesort algorithm.

    >>> mergesort([4, 2, 5, 2, 1])
    [1, 2, 2, 4, 5]
    >>> mergesort([])     # sorting an empty list
    []
    >>> mergesort([1])   # sorting a one-element list
    [1]
    """
    lst1, lst2 = [], []
    for i in range(len(seq)):
        if i % 2 == 0: lst1.append(seq[i])
        else: lst2.append(seq[i])
    return merge(lst1, lst2)
