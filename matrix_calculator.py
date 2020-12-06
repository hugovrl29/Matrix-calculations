def rank_calculator(mat):
    """ Calculates a matrix rank

    Parameter
    ---------
    mat: array of arrays int (tab, tab, int)

    Return
    ------
    mat_rank: matrix rank (int)
    """
    
        

def sub_matrix_calculator(mat, num_r, num_c):
    """Creates a dictionnary containing all the matrix submatrixes

    Parameter
    ---------
    mat: array of integer arrays (tab, tab, int)
    num_r: concerned number row (int)
    num_c: concerned number column (int)

    Return
    ------
    sub_mat: all the matrix submatrixes (dict)
    """
    sub_mat = mat
    del sub_mat[num_r-1]
    for vector in sub_mat:
        del sub_mat[vector][num_c-1]
    return sub_mat

def det_calculator(mat):
    """ Calculates a matrix determinant

    Parameter
    --------
    mat: array of integer arrays (tab, tab, int)

    Return
    ------
    det: matrix det(int)
    """
    if len(mat) == 2:
        det = (mat[0][0]*mat[1][1]) - (mat[0][1]*mat[1][0])
    elif len(mat) == 3:
        sum_diag = (mat[0][0]*mat[1][1]*mat[2][2])+(mat[0][1]*mat[1][2]*[2][0])+(mat[0][2]*mat[1][0]*mat[2][1])
        min_diag = -(mat[0][2]*mat[1][1]*mat[2][0])-(mat[0][1]*mat[1][0]*mat[2][2])-(mat[0][0]*mat[1][2]*mat[2][1])
        det = sum_diag + min_diag
    else:
        minor = {}
        index = 0
        actual_mat = mat
        while len(actual_mat) != 3:
            for number in mat[0]:
                if index % 2 == 0:
                    minor[index] = sub_matrix_calculator(number, 0, number.index)
    return det