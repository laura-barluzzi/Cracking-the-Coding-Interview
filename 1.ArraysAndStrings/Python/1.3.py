class Solution():
    def remove_duplicate_chars(self, string):
      """
      :type string = str
      :rtype = str
      
      >>> Solution().remove_duplicate_chars('abaca')
      'abc'
      
      >>> Solution().remove_duplicate_chars('abc')
      'abc'
      
      >>> Solution().remove_duplicate_chars('')
      ''
      """
      
      return "".join(OrderedDict.fromkeys(string))

if __name__ == '__main__':
    from collections import OrderedDict
    import doctest
    doctest.testmod(verbose=True)
