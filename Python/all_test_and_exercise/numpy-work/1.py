import numpy as np

def interchange(mat, row1, row2):
    a = []
    s = len(mat[row2])
    for i in range(s):
        a.append(mat[row1][i])
        mat[row1][i] = mat[row2][i]
    for i in range(s):
        mat[row2][i] = a[i]
    """
        Row switching. A row within the matrix 'mat' will be switched with another row.

        Args:
            mat (numpy.matrix): the matrix to apply row switching transformation.
            row1 (int): the row index to be switched. The row index is in [0, mat.shape[0]-1]
            row2 (int): the another row index to be switched. The row index is in [0, mat.shape[0]-1]
    """
def scale(mat, row, scale):
    s = len(mat[row])
    for i in range(s):
        mat[row][i] = float(mat[row][i])*scale
    """
        Row multiplication. Each element in a given row will be multiplied by a non-zero constant. It is also known as scaling a row.

        Args:
            mat (numpy.matrix): the matrix to apply row multiplication transformation.
            row (int): the row index to be multiplied. The row index is in [0, mat.shape[0]-1]
            scale (int or float): the multiplier value.
    """

def add(mat, row1, row2, scale):
    s = len(mat[row2])
    for i in range(s):
        mat[row2][i] = mat[row2][i]+mat[row1][i]*scale
