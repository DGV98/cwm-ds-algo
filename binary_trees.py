"""
Tree (root)
Node (value, left_child, right_child)
insert (value)
find(value)
"""

import math


class Node:
    def __init__(self, val):
        self.value: int = val
        self.left_child: Node = None
        self.right_child: Node = None
        self.__class__.__name__ = str(val)

    def __str__(self):
        return self.value


class Tree:
    def __init__(self):
        self.root: Node = None

    def insert(self, val: int):
        node = Node(val)
        if not self.root:
            self.root = node
        else:
            curr = self.root
            while True:
                if val < curr.value:
                    if not curr.left_child:
                        curr.left_child = node
                        break
                    curr = curr.left_child
                elif val > curr.value:
                    if not curr.right_child:
                        curr.right_child = node
                        break
                    curr = curr.right_child

    def find(self, val):
        if not self.root:
            return False
        curr = self.root
        while curr:
            if val == curr.value:
                return True
            elif val < curr.value:
                curr = curr.left_child
            else:
                curr = curr.right_child
        return False


def traverse_pre_order(root: Node):
    if not root:
        return
    print(root.value)
    traverse_pre_order(root.left_child)
    traverse_pre_order(root.right_child)


def traverse_in_order(root: Node):
    if not root:
        return
    traverse_in_order(root.left_child)
    print(root.value)
    traverse_in_order(root.right_child)


def traverse_post_order(root: Node):
    if not root:
        return
    traverse_post_order(root.left_child)
    traverse_post_order(root.right_child)
    print(root.value)


def height(root: Node):
    if not root:
        return -1
    if not root.left_child and not root.right_child:
        return 0
    return 1 + max(height(root.left_child), height(root.right_child))


def minimum(root: Node):
    if not root.left_child and not root.right_child:
        return root.value
    return min(min(minimum(root.left_child), minimum(root.right_child)), root.value)


def is_leaf(node: Node):
    return not node.left_child and not node.right_child


def equal(root1: Node, root2: Node):
    if not root1 and not root2:
        return True
    if root1 and root2:
        return (
            root1.value == root2.value
            and equal(root1.left_child, root2.left_child)
            and equal(root1.right_child, root2.right_child)
        )
    return False


def valid_bst(root: Node, min: int, max: int):
    if not root:
        return True
    return (
        root.value > min
        and root.value < max
        and valid_bst(root.left_child, min, root.value)
        and valid_bst(root.right_child, root.value, max)
    )


if __name__ == "__main__":
    t = Tree()
    t.insert(7)
    t.insert(4)
    t.insert(9)
    t.insert(1)
    t.insert(6)
    t.insert(8)
    t.insert(10)
    t2 = Tree()
    t2.insert(7)
    t2.insert(4)
    t2.insert(9)
    t2.insert(1)
    t2.insert(6)
    t2.insert(8)
    # t2.insert(10)
    print("Pre Order")
    traverse_pre_order(t.root)
    print("In Order:")
    traverse_in_order(t.root)
    print("Post Order")
    traverse_post_order(t.root)
    print(f"Height of the tree is: {height(t.root)}")
    print(f"Minimum of tree is: {minimum(t.root)}")
    print(f"Equal trees t1 and t2: {equal(t.root, t2.root)}")
    print(f"This is a valid BST: {valid_bst(t.root, -math.inf, math.inf)}")
