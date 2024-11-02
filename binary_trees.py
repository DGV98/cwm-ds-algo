"""
Tree (root)
Node (value, left_child, right_child)
insert (value)
find(value)
"""


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


if __name__ == "__main__":
    t = Tree()
    t.insert(7)
    t.insert(4)
    t.insert(9)
    t.insert(1)
    t.insert(6)
    t.insert(8)
    t.insert(10)
    print("Pre Order")
    traverse_pre_order(t.root)
    print("In Order:")
    traverse_in_order(t.root)
    print("Post Order")
    traverse_post_order(t.root)
