#!usr/bin/env python
import unittest
from typing import Optional


class Node(object):
    def __init__(self, node: int, next_node=None):
        self.data = node
        self._next = next_node

    def __repr__(self):
        return str(self.data)


class SingleLinkList(object):
    def __init__(self):
        self.head = None

    def find_by_value(self, value):
        node = self.head
        while node._next and node.data != value:
            node = node._next
        if value == node.data:
            return node

    def find_by_index(self, index: int) -> Optional[Node]:
        pointer = self.head
        position = 0
        while position < index and pointer:
            pointer = pointer._next
            position += 1
        return pointer

    def insert_value_to_head(self, value):
        node = Node(value)
        self.insert_node_to_head(node)

    def insert_node_to_head(self, node: Node):
        node._next = self.head
        self.head = node

    def insert_value_after(self, node: Node, value: int):
        new_node = Node(value)
        self.insert_node_after(new_node, node)

    def insert_node_after(self, new_node: Node, node: Node):
        new_node._next = node._next
        node._next = new_node

    def insert_value_before(self, node: Node, value: int):
        new_node = Node(value)
        self.insert_node_before(node, new_node)

    def insert_node_before(self, node: Node, new_node: Node):
        if not self.head or not node or not new_node:
            return
        if self.head == node:
            self.insert_node_to_head(new_node)
        current = self.head
        while current._next != node:
            current = current._next
        if not current._next:
            return
        new_node._next = node
        current._next = new_node

    def delete_by_node(self, node: Node):
        if not self.head or not node:
            return
        if node is self.head:
            self.head = self.head._next
            return
        pro_node = current = self.head
        while current != node:
            pro_node = current
            current = current._next
        if pro_node._next == node:
            pro_node._next = pro_node._next._next

    def __repr__(self) -> str:
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current._next
        return ' -> '.join(str(value) for value in values)

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node._next


class TestDict(unittest.TestCase):

    def setUp(self) -> None:
        self.link = SingleLinkList()
        for i in range(20):
            self.link.insert_value_to_head(i)

    def test_init(self):
        self.assertEqual(str(self.link),
                         '19 -> 18 -> 17 -> 16 -> 15 -> 14 -> 13 -> 12 -> 11 -> '
                         '10 -> 9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 0')

    def test_find_by_value(self):
        node5 = self.link.find_by_value(5)
        self.assertEqual(node5.data, 5)

    def test_find_last_by_value(self):
        node0 = self.link.find_by_value(0)
        self.assertEqual(node0.data, 0)

    def test_find_by_index(self):
        node18 = self.link.find_by_index(1)
        self.assertEqual(18, node18.data)
        node0 = self.link.find_by_index(19)
        self.assertEqual(0, node0.data)
        node_none = self.link.find_by_index(20)
        self.assertIsNone(node_none)

    def test_delete_node(self):
        node10 = self.link.find_by_value(10)
        self.link.delete_by_node(node10)
        self.assertEqual(str(self.link),
                         '19 -> 18 -> 17 -> 16 -> 15 -> 14 -> 13 -> 12 -> 11 -> '
                         '9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 0')

    def test_delete_head_node(self):
        self.link.delete_by_node(self.link.head)
        self.assertEqual(str(self.link),
                         '18 -> 17 -> 16 -> 15 -> 14 -> 13 -> 12 -> 11 -> '
                         '10 -> 9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 0')

    def test_delete_last_node(self):
        last_node = self.link.find_by_value(0)
        self.link.delete_by_node(last_node)
        self.assertEqual(str(self.link),
                         '19 -> 18 -> 17 -> 16 -> 15 -> 14 -> 13 -> 12 -> 11 -> '
                         '10 -> 9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1')


if __name__ == '__main__':
    unittest.main()
