class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None

    def addFirst(self, val):
        node = Node(val)
        if not self.first and not self.last:
            self.first = node
            self.last = node
        else:
            node.next = self.first
            self.first = node

    def addLast(self, val):
        node = Node(val)
        if not self.first and not self.last:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def deleteFirst(self):
        if self.first:
            self.first = self.first.next

    def deleteLast(self):
        if self.first and self.first.next:
            node = self.first
            while node.next.next:
                node = node.next
            node.next = None
            self.last = node
        else:
            self.first = None
            self.last = None

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


if __name__ == "__main__":
    ll = LinkedList()
    print(ll)
    ll.addLast(1)
    ll.addLast(2)
    ll.addLast(3)
    ll.addFirst(50)
    print(ll.indexOf(50))  # 0
    print(ll.indexOf(100))  # -1
    print(ll.contains(3))  # True
    ll.deleteFirst()
    print(ll)
    ll.deleteLast()
    print(ll)
    ll.deleteLast()
    ll.deleteLast()
    ll.deleteLast()
    ll.deleteFirst()
    print(ll)
