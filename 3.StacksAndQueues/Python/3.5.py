class MyQueue:
    def __init__(self):
        self.stack = []
        self.reversed_stack = []

    def add(self, item):
        """
        >>> queue = MyQueue()
        >>> queue.add('Laura')
        ['Laura']
        >>> queue.add('Vera')
        ['Laura', 'Vera']
        >>> queue.add('Martina')
        ['Laura', 'Vera', 'Martina']
        """
        self.stack.append(item)
        return self.stack

    def peek(self):
        """
        >>> queue = MyQueue()
        >>> queue.add('Laura')
        ['Laura']
        >>> queue.add('Vera')
        ['Laura', 'Vera']
        >>> queue.add('Martina')
        ['Laura', 'Vera', 'Martina']
        >>> queue.peek()
        'Laura'
        >>> queue.peek()
        'Laura'
        """
        if not self.reversed_stack and self.stack:
            self.reversed_stack = self.populate_reversed_stack()

        return self.reversed_stack[self.last_i(self.reversed_stack)]

    def pop(self):
        """
        >>> queue = MyQueue()
        >>> queue.add('Laura')
        ['Laura']
        >>> queue.add('Vera')
        ['Laura', 'Vera']
        >>> queue.add('Martina')
        ['Laura', 'Vera', 'Martina']
        >>> queue.pop()
        'Laura'
        >>> queue.pop()
        'Vera'
        """
        if not self.reversed_stack and self.stack:
            self.reversed_stack = self.populate_reversed_stack()
        return self.reversed_stack.pop()

    def populate_reversed_stack(self):
        """
        >>> queue = MyQueue()
        >>> queue.populate_reversed_stack()
        []
        >>> queue.add('First')
        ['First']
        >>> queue.add('Second')
        ['First', 'Second']
        >>> queue.add('Third')
        ['First', 'Second', 'Third']
        >>> queue.populate_reversed_stack()
        ['Third', 'Second', 'First']
        """
        return [self.stack.pop() for _ in range(len(self.stack) - 1, -1, -1)]

    def last_i(self, stack):
        return len(stack) - 1


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)