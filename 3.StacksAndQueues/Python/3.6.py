class Solution:
    def __init__(self, stack):
        self.given_s = stack
        self.sorted_s = []

    def sort_stack(self):
        """
        >>> solution = Solution(['z', 'b', 'a'])
        >>> solution.sort_stack()
        ['a', 'b', 'z']
        """
        while not self.is_empty(self.given_s):
            peeked = self.pop(self.given_s)
            sorted_is_not_empty = not self.is_empty(self.sorted_s)

            while sorted_is_not_empty and peeked < self.peek(self.sorted_s):
                self.given_s.append(self.pop(self.sorted_s))
            self.sorted_s.append(peeked)

        return self.sorted_s

    def peek(self, stack):
        """
        >>> solution = Solution([1, 2, 3])
        >>> solution.peek(solution.given_s)
        3
        """
        return stack[len(stack) - 1]

    def pop(self, stack):
        """
        >>> solution = Solution([1, 2, 3])
        >>> solution.pop(solution.given_s)
        3
        """
        return stack.pop()

    def is_empty(self, stack):
        """
        >>> solution = Solution([])
        >>> solution.is_empty(solution.given_s)
        True
        >>> solution.given_s = [1]
        >>> solution.is_empty(solution.given_s)
        False
        """
        return True if not len(stack) else False


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)