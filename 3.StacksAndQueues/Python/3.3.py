class SetOfStack:
    def __init__(self):
        self.stacks = []
        self.max_len = 5

    def sub_stack_is_full(self, sub_stack):
        """
        >>> set = SetOfStack()
        >>> set.stacks = [[1, 2, 3, 4, 5], [3]]
        >>> set.sub_stack_is_full(set.stacks[0])
        True
        >>> set.sub_stack_is_full(set.stacks[1])
        False
        """
        return True if len(sub_stack) == self.max_len else False

    def last_sub_stack(self):
        """
        >>> set = SetOfStack()
        >>> set.stacks = [[1, 2, 3, 4, 5], [3]]
        >>> set.last_sub_stack()
        [3]
        >>> set.stacks = [[1, 2, 3, 4, 5], [3, 3, 3]]
        >>> set.last_sub_stack()
        [3, 3, 3]
        """
        num_stacks = len(self.stacks)
        return self.stacks[num_stacks - 1]

    def push(self, item):
        """
        >>> set = SetOfStack()
        >>> set.stacks = [[1, 2, 3, 4, 5], [3]]
        >>> set.push(5)
        [[1, 2, 3, 4, 5], [3, 5]]
        >>> set.stacks = [[1, 2, 3, 4, 5]]
        >>> set.push('a')
        [[1, 2, 3, 4, 5], ['a']]
        """
        last_sub_stack = self.last_sub_stack()
        if self.sub_stack_is_full(last_sub_stack):
            self.stacks.append([item])
        else:
            last_sub_stack.append(item)
        return self.stacks

    def pop(self):
        """
        >>> set = SetOfStack()
        >>> set.stacks = [[1, 2, 3, 4, 5], [3]]
        >>> set.pop()
        3
        >>> set.stacks = [[1, 2, 3, 4, 5], [3, 1]]
        >>> set.pop()
        1
        """
        popped = self.last_sub_stack().pop()
        sub_stack_is_empty = len(self.last_sub_stack()) == 0
        if sub_stack_is_empty:
            self.stacks.pop()
        return popped

    def popAt(self, index_sub_stack):
        """
        >>> set = SetOfStack()
        >>> set.stacks = [[1, 2, 3, 4, 5], [3]]
        >>> set.popAt(0)
        5
        >>> set.stacks = [[1, 2, 3, 4, 5], [3, 1]]
        >>> set.popAt(1)
        1
        """
        return self.stacks[index_sub_stack].pop()

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)