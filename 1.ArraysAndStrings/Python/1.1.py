class Solution:
    def has_unique_chars(self, string):
        """
        :type string: str
        :rtype: Boolean
        
        >>> Solution().has_unique_chars('abcdefg')
        True
        
        >>> Solution().has_unique_chars('')
        True
        
        >>> Solution().has_unique_chars('abcabc')
        False
        """
        return True if len(set(string)) == len(string) else False

    def has_unique_chars_2(self, string):
        """
        :type string: str
        :rtype: Boolean
        
        >>> Solution().has_unique_chars_2('abcdefg')
        True
        
        >>> Solution().has_unique_chars_2('')
        True
        
        >>> Solution().has_unique_chars_2('abcabc')
        False
        """
        are_all_unique = True
        new_string = ''
        i = 0
        
        while are_all_unique and i < len(string): 
          if string[i] not in new_string:
            new_string += string[i]
          else:
            are_all_unique = False
          i += 1

        return are_all_unique

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
