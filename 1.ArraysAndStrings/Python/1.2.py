class Solution():
  def reverse_c_string(self, string):
    """
    :type string = str
    :rtype = str
    
    >>> Solution().reverse_c_string('abc$')
    'cba$'
    
    >>> Solution().reverse_c_string('a$')
    'a$'
    
    >>> Solution().reverse_c_string('')
        
    """
    
    if len(string) == 0:
      return None
   
    if len(string) == 2:
      return string
    
    rev_string = ''
        
    for i in range(0, len(string) -1):
      rev_string = string[i] + rev_string
    
    return rev_string+string[len(string)-1]


if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)

