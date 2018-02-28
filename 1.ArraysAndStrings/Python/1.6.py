class Solution():
  def rotate_matrix(self, matrix):
    """
    :type matrix = list
    :rtype = list
    
    >>> Solution().rotate_matrix([[1, 'a'], [2, 'b']])
    [['a', 'b'], [1,2]]
    
    >>> Solution().rotate_matrix([[1, 'a'], [2, 'b']])
    [['a', 'b'], [1,2]]
        
    """
    len_matrix = len(matrix)
    
    for i in range(0, len_matrix):
      new_col = []

      for j in range(0, len_matrix):
        new_col.append(matrix[j][i])

      matrix.append(new_col)

    return matrix[len_matrix:][::-1]

if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)
