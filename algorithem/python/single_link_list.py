#!usr/bin/env python

class Node(object):
	def __init__(self, node: int, value=None):
		self._node = None
		self._value = value

	def __repr__(self):
		return f'{self._node}: f{self.value}'



if __name__ == '__main__':
	node = Node(1)
	print(node)
