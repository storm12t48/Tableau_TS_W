
import numpy as np

def rowsum(matrix):
    """
    :param matrix (list): A list of lists where each inner list represents a row.
    :returns: (list) A list containing the sum of each row.
    """
    sum_matrix=np.sum(matrix, axis = 1)
    return sum_matrix

print(rowsum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # Should print [6, 15, 24]
