class Node:
    def __init__(self, value=None, next=None):
      self.value = value
      self.next = next

    def __str__(self):
      return str(self.value)

def print_list(node):
    result = []
    while node is not None:
        result.append(str(node.value))
        node = node.next
    return " ".join(result)


class Solution:
    """Assumtion: node given must be in the middle of the linked list"""

    def get_length(self, head):
        """
        :param head:
        :return: length:

        >>> head = Node("1", (Node("2", Node("mid", Node("3", Node("4"))))))
        >>> Solution().get_length(head)
        5
        """
        if head is None:
            return
        length = 0
        while head is not None:
            head = head.next
            length += 1
        return length

    def remove_mid_node(self, head, node):
        """
        :param node:
        :return: None:

        >>> head = Node("1", (Node("2", Node("mid", Node("3", Node("4"))))))
        >>> Solution().remove_mid_node(head, head.next.next)
        """
        middle = self.get_length(head) // 2
        previous = head
        current = head.next

        for _ in range(middle - 1):
            previous = current
            current = current.next

        if current == node:
            previous.next = current.next
            current.next = None

        if current != node:
            raise ValueError


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)