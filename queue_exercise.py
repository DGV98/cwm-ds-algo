from collections import deque


def reverse_queue(q: deque):
    stack = []
    while q:
        stack.append(q.popleft())
    new_q = deque([])
    while stack:
        new_q.append(stack.pop())
    return new_q


class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, element):
        self.q.append(element)

    def dequeue(self):
        return self.q.pop(0)

    def peek(self):
        return self.q[0]

    def isEmpty(self):
        return not self.q

    def reverse(self, k):
        i, j = 0, k - 1
        while j > i:
            val = self.q[j]
            self.q[j] = self.q[i]
            self.q[i] = val
            j -= 1
            i += 1


class stackQueue:
    def __init__(self) -> None:
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        self.stack1.append(element)

    def dequeue(self):
        if not self.stack1 and not self.stack2:
            return None

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


class PriorityQueue:
    def __init__(self):
        self.q = deque()

    def enqueue(self, item):
        if not self.q:
            self.q.append(item)
        elif self.q[0] > item:
            self.q.appendleft(item)
        else:
            self.q.append(item)
            i = len(self.q) - 1
            while i - 1 > 0:
                if self.q[i - 1] > item:
                    self.q[i] = self.q[i - 1]
                i -= 1
            self.q[i] = item

    def dequeue(self):
        return self.q.popleft()


class StackWith2Queues:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, item):
        self.q1.append(item)

    def pop(self):
        while self.q1:
            self.q2.append()


if __name__ == "__main__":
    q = deque([1, 2, 3, 4])
    print(reverse_queue(q))
    q = PriorityQueue()
    q.enqueue(1)
    q.enqueue(5)
    q.enqueue(4)
    q.enqueue(0)
    print(q.q)
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.reverse(2)
    print(q.q)
