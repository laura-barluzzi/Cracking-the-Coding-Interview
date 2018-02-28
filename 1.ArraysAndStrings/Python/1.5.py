class Solution():
  def replace_space(self, string):
    """
    :type string = str
    rtype = str
    
    >>> Solution().replace_space('Hello world')
    'Hello%20world'
    
    >>> Solution().replace_space('')
    ''
    
    >>> Solution().replace_space('3   spaces')
    '3%20%20%20spaces'
    """
    # p = re.compile('\s')
    # return p.sub('%20', string)
    
    return string.replace(' ', '%20')
    
    
if __name__ == '__main__':
  import re
  import doctest
  doctest.testmod(verbose=True)
