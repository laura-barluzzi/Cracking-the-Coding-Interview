class Node:
	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next

	def __str__(self):
		return str(self.value)


class Solution:
	def get_node_in_pos(self, head, n):
		"""
		>>> linked_list = Node(1, Node(2, Node(3, Node(4, Node(5)))))
		>>> Solution().get_node_in_pos(linked_list, 3)
		3

		>>> Solution().get_node_in_pos(linked_list, 2)
		4
		"""

		nth_last_node = head

		for _ in range(n):
			head = head.next

			if head is None:
				raise ValueError

		while head is not None:
			head = head.next
			nth_last_node = nth_last_node.next

		return nth_last_node.value


if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
