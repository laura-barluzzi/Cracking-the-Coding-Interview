class Stack:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, item):
        """
        >>> stack = Stack()
        >>> stack.stack = []
        >>> stack.push(5)
        >>> stack.stack = [1, 2, 3, 4, 5]
        >>> stack.push(6)
        """
        if len(self.mins) == 0 or item < self.min():
            self.mins.append(item)
        else:
            self.mins.append(self.min())
        self.stack.append(item)

    def min(self):
        """
        >>> stack = Stack()
        >>> stack.stack = []
        >>> stack.push(4)
        >>> stack.min()
        4
        >>> stack.push(44)
        >>> stack.push(5)
        >>> stack.push(6)
        >>> stack.push(1)
        >>> stack.min()
        1
        >>> stack.pop()
        1
        >>> stack.min()
        4
        """
        len_mins = len(self.mins)
        if not len_mins:
            return
        return self.mins[len(self.mins) - 1]

    def pop(self):
        """
        >>> stack = Stack()
        >>> stack.stack = [1, 2, 3, 33]
        >>> stack.pop()
        33
        """
        popped = self.stack.pop()
        if popped == self.min():
            self.mins.pop()
        return popped


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
