def add_matrices(x, y):
    """
    >>> matrix1 = [[1, 3],
    ...            [2, 0]]
    >>> matrix2 = [[-3, 0],
    ...            [1, 2]]
    >>> add_matrices(matrix1, matrix2)
    [[-2, 3], [3, 2]]
    """
    
    #return [[x[i][0]+ y[i][0], x[i][1]+y[i][1]] for i in range(len(x))]
    return [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
