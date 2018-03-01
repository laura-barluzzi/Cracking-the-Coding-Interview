class Node:
    def __init__(self, value=None, next=None):
      self.value = value
      self.next = next

    def __str__(self):
      return str(self.value)

node_1 = Node("1")
node_2 = Node("2")
node_3 = Node("3")
node_4 = node_2
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

def print_list(node):
    result = []
    while node is not None:
        result.append(node.value)
        node = node.next
    return int("".join(result))

class Solution:
    def find_loop_beginning(self, head):
        node1 = head
        node2 = head

        while node2.next is not None:
            node1 = node1.next
            node2 = node2.next.next
            if node1 == node2:
                break

        node1 = head
        while node1 != node2:
            node1 = node1.next
            node2 = node2.next

        return node2

    def find_loop_beginning_test(self, head, node_start_loop):
        """
        >>> node_1 = Node("1")
        >>> node_2 = Node("2")
        >>> node_3 = Node("3")
        >>> node_4 = node_2
        >>> node_1.next = node_2
        >>> node_2.next = node_3
        >>> node_3.next = node_4
        >>> Solution().find_loop_beginning_test(node_1, node_2)
        True
        """

        if node_start_loop == self.find_loop_beginning(head):
            return True
        else:
            return False

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)