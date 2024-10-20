class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return not self.stack


class minStack:
    def __init__(self):
        self.stack = []
        self.min = 0

    def push(self, element):
        if element < self.min:
            self.min = element
        self.stack.append(element)

    def pop(self):
        el = self.stack.pop()
        if el == self.min:
            self.min = min(self.stack)
        return el

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return not self.stack

    def min(self):
        return self.min


if __name__ == "__main__":
    stack = Stack()
    stack.push(5)
    stack.push(7)
    print(stack.peek())
    print(stack.pop())
    print(stack.isEmpty())
    stack.pop()
    print(stack.isEmpty())
