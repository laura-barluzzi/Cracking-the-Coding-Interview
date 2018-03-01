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


class Solution1:
    def remove_duplicates(self, node, pre_node=None, already_found={}, first=None):
        """
        >>> linked_list = Node(1, Node(2, Node(3, Node(4, Node(3)))))
        >>> Solution1().remove_duplicates(linked_list)
        1 2 3 4
        """

        if pre_node is None and node is not None:
            first = node

        if node.value in already_found:
           if node.next is None:
              pre_node.next = None
           else:
              pre_node.next = node.next.next
           node.next = None 
        
        else:
            already_found[node.value] = node.value
        
        if node.next is not None:
            pre_node = node
            self.remove_duplicates(node.next, pre_node, already_found, first)
        
        else:
            return print(print_list(first))

class Solution2:
    def remove_duplicates(self, head):
        """
        >>> head = Node(1, Node(2, Node(3, Node(3, Node(3)))))
        >>> Solution2().remove_duplicates(head)
        1 2 3
        """
        previous = head
        current = previous.next

        while current is not None:
            runner = head
            while runner is not current:
                if runner.value == current.value:
                    previous.next = current.next
                    current = current.next
                    break
                runner = runner.next

            if runner == current:
                previous = current
                current = current.next

        return print(print_list(head))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
