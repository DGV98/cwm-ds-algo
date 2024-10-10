class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def addFirst(self, val):
        node = Node(val)
        if not self.first:
            self.first = node
            self.last = node
        else:
            node.next = self.first
            self.first = node
        self.size += 1

    def addLast(self, val):
        node = Node(val)
        if not self.first:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.size += 1

    def deleteFirst(self):
        if self.first == self.last:
            self.first = None
            self.last = None
            self.size = 0
        if self.first:
            self.first = self.first.next
            self.size -= 1

    def deleteLast(self):
        if self.first and self.first.next:
            node = self.first
            while node.next.next:
                node = node.next
            node.next = None
            self.last = node
            self.size -= 1
        else:
            self.first = None
            self.last = None
            self.size = 0

    def contains(self, val):
        node = self.first
        while node:
            if node.value == val:
                return True
            node = node.next
        return False

    def indexOf(self, val):
        node = self.first
        i = 0
        while node.next:
            if node.value == val:
                return i
            node = node.next
            i += 1
        return -1

    def __repr__(self):
        if not self.first:
            return "[]"
        representation = []
        node = self.first
        while node:
            representation.append(node.value)
            node = node.next
        return str(representation)

    def size(self):
        return self.size

    def reverse(self):
        if not self.first:
            return
        prev = None
        node = self.first
        self.last = node
        next_node = node.next
        while next_node:
            node.next = prev
            prev = node
            node = next_node
            next_node = next_node.next
        node.next = prev
        self.first = node

    def get_kth_from_the_end(self, k):
        if not self.first:
            return
        if k > self.size or k <= 0:
            return
        i = 0
        curr = self.first
        node = self.first
        while i < k - 1 and node:
            node = node.next
            i += 1
        while node.next:
            curr = curr.next
            node = node.next
        return curr

    def print_middle(self):
        if not self.first:
            return
        if self.first == self.last:
            return (self.first.value)
        if self.first.next == self.last:
            return (self.first.value, self.last.value)
        slow = self.first
        fast = self.first
        while fast.next:
            if not fast.next.next:
                return (slow.value, slow.next.value)
            slow = slow.next
            fast = fast.next.next
        return (slow.value)

    def has_loop(self):
        if not self.first:
            return False
        if self.first == self.last:
            return False
        slow = self.first
        fast = self.first
        while fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    ll = LinkedList()
    ll.addLast(10)
    ll.addLast(20)
    print(ll.print_middle())
    # ll.reverse()
    print(ll)
    # ll.addFirst(50)
    # print(ll.indexOf(50))  # 0
    # print(ll.indexOf(100))  # -1
    # print(ll.contains(3))  # True
    # ll.deleteFirst()
    # print(ll)
    # ll.deleteLast()
    # print(ll)
    # ll.deleteLast()
    # ll.deleteLast()
    # ll.deleteLast()
    # ll.deleteFirst()
    # print(ll)
