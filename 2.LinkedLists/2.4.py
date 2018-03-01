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
    return int("".join(result))

class Solution:
    def get_num(self, head):
        """
        :param head:
        :return: num:

        >>> head1 = Node(3, Node(1, Node(5)))
        >>> head2 = Node(5, Node(9, Node(2)))
        >>> Solution().get_num(head1)
        513
        >>> Solution().get_num(head2)
        295
        """
        num = 0
        i = 0
        while head is not None:
            if i == 0:
                num += head.value
                i += 10
            else:
                num += i * head.value
                i *= 10
            head = head.next

        return num

    def sum(self, head1, head2):
        """
        :return: sum:

        >>> head1 = Node(3, Node(1, Node(5)))
        >>> head2 = Node(5, Node(9, Node(3)))
        >>> Solution().sum(head1, head2)
        908
        """
        return self.get_num(head1) + self.get_num(head2)

    def sum_to_list(self, head1, head2):
        """
        :param head1:
        :param head2:
        >>> head1 = Node(3, Node(1, Node(5)))
        >>> head2 = Node(5, Node(9, Node(3)))
        >>> Solution().sum_to_list(head1, head2)
        809
        """
        sum_res = self.sum(head1, head2)
        sum_str = str(sum_res)
        num_digits = len(sum_str)

        head = Node(sum_str[num_digits - 1])
        current_node = head
        while num_digits != 0:
            i = num_digits - 1

            if i != 0:
                next_node = Node(sum_str[i-1])
                current_node.next = next_node

            current_node = next_node
            num_digits -= 1

        print(print_list(head))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)