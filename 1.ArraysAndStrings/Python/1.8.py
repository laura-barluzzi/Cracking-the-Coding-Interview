class Solution():
  def is_a_rotation(self, s1, s2):
    """
    :type s1 = str
    :type s2 = str
    rtype = Boolean
    
    >>> Solution().is_a_rotation('Water', 'terWa')
    True
    
    >>> Solution().is_a_rotation('Water', 'Water')
    True
    
    >>> Solution().is_a_rotation('Water', '')
    False
    
    >>> Solution().is_a_rotation('Water', 'retaW')
    False
    """

    end_and_start = str(s1[len(s1)-1] + s1[0])
    
    if s1 == s2:
      return True
    
    elif len(s1) == len(s2) and end_and_start in s2:
      start_sub = s2.index(end_and_start[1])
      end_sub = len(s2)
      return self.recursive_check(s1, s2, start_sub, end_sub)
      
    else:
      return False
    
  def recursive_check(self, s1, s2, start, end, count=0):
    is_ss = self.isSubstring(s1, s2[start:end])
    if not is_ss:
        return False
    
    if count == 0:
      return self.recursive_check(s1, s2, 0, start, 1)
    elif count == 1:
      return is_ss
    else:
      return False
 
  def isSubstring(self, main_string, sub_string):
    return True if sub_string in main_string else False
    
    
if __name__ == '__main__':

  import doctest
  doctest.testmod(verbose=True)
