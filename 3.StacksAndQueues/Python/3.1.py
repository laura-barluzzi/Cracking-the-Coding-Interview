"""
Describe how you could use a single array to implement three stacks
"""

class Solution:
    def __init__(self):
        self.stack_names = {'order': 0, 'letters': 1, 'numbers': 2}
        self.three_stacks = [[], [], []]

    def add_item(self, stack_name, item):
        """
        >>> stacks = Solution()
        >>> stacks.add_item('order', 'first')
        [['first'], [], []]
        >>> stacks.add_item('order', 'second')
        [['first', 'second'], [], []]
        >>> stacks.add_item('numbers', 1)
        [['first', 'second'], [], [1]]
        >>> stacks.add_item('numbers', 2)
        [['first', 'second'], [], [1, 2]]
        >>> stacks.add_item('letters', 'A')
        [['first', 'second'], ['A'], [1, 2]]
        """

        i = self.get_stack(stack_name)
        self.three_stacks[i].append(item)
        return self.three_stacks

    def pop_item(self, stack_name):
        """
        >>> stacks = Solution()
        >>> stacks.three_stacks = [['first', 'last'], ['A'], [1, 2, 3]]
        >>> stacks.pop_item('numbers')
        [['first', 'last'], ['A'], [1, 2]]
        >>> stacks.pop_item('order')
        [['first'], ['A'], [1, 2]]
        """

        i = self.get_stack(stack_name)
        self.three_stacks[i].pop()
        return self.three_stacks

    def get_stack(self, stack_name):
        return self.stack_names[stack_name]

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

