class Node:
    def __init__(self, value=None, next=None):
      self.value = value
      self.next = next
    
    def __str__(self):
      return str(self.value)

node1 = Node("1")
node2 = Node("2")
node3 = Node("3")
node4 = Node("2")
node5 = Node("2")
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def print_list(node):
    result = []
    while node is not None:
        result.append(node.value)
        node = node.next
    return(" ".join(result))


class Solution:
    def remove_duplicates(self, node, pre_node=None, already_found={}, first=None):
        """

        >>> Solution().remove_duplicates(node1)
        1 2 3
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


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
