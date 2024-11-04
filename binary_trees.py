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
    if root1 and not root2:
        return False
    if not root1 and root2:
        return False
    if not root1 and not root2:
        return True
    return (
        equal(root1.left_child, root2.left_child)
        and equal(root1.right_child, root2.right_child)
        and root1.value == root2.value
    )


def node_k_distance(root: Node, k: int):
    if not root:
        return
    if k == 0 and root:
        print(root.value)
        return
    node_k_distance(root.left_child, k - 1)
    node_k_distance(root.right_child, k - 1)


def get_nodes_k_distance(root: Node, k: int, elements: list):
    if not root:
        return
    if k == 0:
        elements.append(root.value)
    get_nodes_k_distance(root.left_child, k - 1, elements)
    get_nodes_k_distance(root.right_child, k - 1, elements)


def bfs(root: Node):
    levels = height(root)
    i = 0
    while i <= levels:
        nodes = []
        get_nodes_k_distance(root, i, nodes)
        for num in nodes:
            print(num)
        i += 1


def size(root: Node):
    if not root:
        return 0
    return 1 + size(root.left_child) + size(root.right_child)


def count_leaves(root: Node):
    if not root.left_child and not root.right_child:
        return 1
    return count_leaves(root.left_child) + count_leaves(root.right_child)


def find_max(root: Node):
    if not root.left_child and not root.right_child:
        return root.value
    return max(max(find_max(root.left_child), find_max(root.right_child)), root.value)


def find_recursive(root: Node, val: int):
    if not root:
        return False
    if root.value == val:
        return True
    return find_recursive(root.left_child, val) or find_recursive(root.right_child, val)


def are_siblings(root: Node, x: int, y: int):
    if not root.left_child or not root.right_child:
        return False
    if root.left_child.value == x and root.right_child.value == y:
        return True
    if root.left_child.value == y and root.right_child.value == x:
        return True
    return are_siblings(root.left_child, x, y) or are_siblings(root.right_child, x, y)


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
    t2.insert(10)
    print("Pre Order")
    traverse_pre_order(t.root)
    print("In Order:")
    traverse_in_order(t.root)
    print("Post Order")
    traverse_post_order(t.root)
    print(f"Height of the tree is: {height(t.root)}")
    print(f"Minimum of tree is: {minimum(t.root)}")
    print(f"Equal trees t1 and t2: {equal(t.root, t2.root)}")
    print(f"Nodes 1 away from root:")
    node_k_distance(t.root, 0)
    bfs(t.root)
    print(f"Size of tree: {size(t.root)}")
    print(f"Number of leaves: {count_leaves(t.root)}")
    print(f"The max of the tree is: {find_max(t.root)}")
    print(f"8 is in the tree: {find_recursive(t.root, 8)}")
    print(f"40 is not in the tree: {find_recursive(t.root, 40)}")
    print(f"4 and 9 are siblings: {are_siblings(t.root, 4, 9)}")
    print(f"4 and 10 are not siblings: {are_siblings(t.root, 4, 10)}")
