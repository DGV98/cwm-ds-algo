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
        prev = None
        node = self.first
        self.last = node
        next_node = node.next
        while next_node:
            print(node.value)
            node.next = prev
            prev = node
            node = next_node
            next_node = next_node.next
        node.next = prev
        self.first = node


if __name__ == "__main__":
    ll = LinkedList()
    print(ll)
    ll.addLast(1)
    ll.addLast(2)
    ll.addLast(3)
    ll.reverse()
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
