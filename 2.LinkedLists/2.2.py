class Node:
    def __init__(self, value=None, next=None):
      self.value = value
      self.next = next
    
    def __str__(self):
      return str(self.value)

node1 = Node("1")
node2 = Node("2")
node3 = Node("3")
node4 = Node("4")
node5 = Node("5")
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

class Solution:
    def __init__(self):
        self.linked_list = {}
    
    def get_node_in_pos(self, node, pos, i=1):
        """
        >>> Solution().get_node_in_pos(node1, 3)
        3
        
        >>> Solution().get_node_in_pos(node1, 2)
        4
        """
        self.linked_list[i] = node
        
        if node.next is not None:
            self.get_node_in_pos(node.next, pos, i+1)
        else:
            length = len(self.linked_list)
            key = length - pos + 1
            node_in_pos = self.linked_list[key]
            print(node_in_pos.value)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
