class Solution():
  def are_anagrams(self, A, B):
    """
    :type A = str
    :type B = str
    rtype = Boolean
    
    >>> Solution().are_anagrams('abcde', 'badce')
    True
    
    >>> Solution().are_anagrams('', '')
    True
    
    >>> Solution().are_anagrams('', 'abc')
    False
    
    >>> Solution().are_anagrams('abcde', 'ab')
    False
    """
    if len(A) == len(B):
      return True if sorted(A) == sorted(B) else False
    else:
      return False
    
    
if __name__ == '__main__':

  import doctest
  doctest.testmod(verbose=True)
