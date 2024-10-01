import math


class Array:
    def __init__(self, length) -> None:
        self.array = [None] * length
        self.last_index = -1

    def expand(self):
        self.array = self.array + ([None] * len(self.array))

    def insert(self, value):
        self.last_index += 1
        if self.last_index == len(self.array):
            self.expand()
            self.array[self.last_index] = value
        else:
            self.array[self.last_index] = value

    def __repr__(self):
        return str(self.array[: self.last_index + 1])

    def removeAt(self, index):
        if index < 0:
            return ValueError("Index not in range")
        while index < self.last_index:
            self.array[index] = self.array[index + 1]
            index += 1
        self.array[index] = None
        self.last_index -= 1

    def indexOf(self, element):
        for i, el in enumerate(self.array):
            if el == element:
                return i
        return -1

    def max(self):
        # Runtime O(n)
        maximum = -math.inf
        for i in self.array:
            maximum = max(maximum, i)
        return maximum

    def intersect(self, array):
        # Runtime O(n^2)
        intersection = set()
        for i in self.array:
            if i in array.array:
                intersection.add(i)
        return intersection

    def reverse(self):
        # Runtime O(n)
        i, j = 0, self.last_index
        while i < j:
            val = self.array[j]
            self.array[j] = self.array[i]
            self.array[i] = val
            i += 1
            j -= 1

    def insertAt(self, item, index):
        self.last_index += 1
        if self.last_index == len(self.array):
            self.expand()
        if index == self.last_index:
            self.array[index] = item
        elif index < self.last_index:
            i, j = index, self.last_index
            while j > i:
                self.array[j] = self.array[j - 1]
                j -= 1
            self.array[index] = item


if __name__ == "__main__":
    array = Array(3)
    array.insert(10)
    array.insert(20)
    array.insert(30)
    array.insert(40)
    print(array)
    array.removeAt(1)
    print(array)
    array2 = Array(3)
    array2.insert(10)
    array2.insert(20)
    array2.insert(30)
    array2.insert(40)
    print(array.indexOf(400))
    print(array.intersect(array2))
    reverse_array = Array(4)
    reverse_array.insert(1)
    reverse_array.insert(2)
    reverse_array.insert(3)
    reverse_array.insert(4)
    reverse_array.reverse()
    print(reverse_array)
    insert_array = Array(3)
    insert_array.insert(10)
    insert_array.insert(20)
    insert_array.insert(30)
    insert_array.insertAt(50, 1)
    print(insert_array)
