class Solution():
  def set_adiacent_to_zero(self, matrix):
    """
    :type matrix = list
    :rtype = list
    
    >>> Solution().set_adiacent_to_zero([[1, 'a', 0], [2, 'b', 20]])
    [[0, 0, 0], [2, 'b', 0]]
    
    >>> Solution().set_adiacent_to_zero([[1, 2, 0], [3, 0, 4], [0, 5, 6], [7, 8, 9]])
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    >>> Solution().set_adiacent_to_zero([[1, 'a', 11], [2, 'b', 22]])
    [[1, 'a', 11], [2, 'b', 22]]
        
    """
    rows_to_zero = [[] for i in range(0, len(matrix))]
    
    cols_to_zero = [[] for i in range(0, len(matrix[0]))]
    
    for i in range(0, len(matrix)):
      for j in range(0, len(matrix[i])):
        if matrix[i][j] == 0:
          rows_to_zero[i] = 1
          cols_to_zero[j] = 1
    
    for i in range(0, len(matrix)):
      for j in range(0, len(matrix[i])):
        if rows_to_zero[i] == 1 or cols_to_zero[j] == 1:
          matrix[i][j] = 0
          
          
    #for i in range(0, len(matrix)): # O(N)      
      
      #if 0 in matrix[i]: # O(N)
        #index_to_zero.append(matrix[i].index(0)) # O(N)
        #matrix[i] = [0 for item in matrix[i]] # O(N)
      
      #for index in index_to_zero: # O(N
        #matrix[i][index] = 0
   
    return matrix
      

if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)
