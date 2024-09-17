class Array:
    def __init__(self, length) -> None:
        self.array = [None] * length
        self.last_index = -1

    def insert(self, value):
        self.last_index += 1
        if self.last_index == len(self.array):
            self.array = self.array + [value]
        else:
            self.array[self.last_index] = value

    def __repr__(self):
        return str(self.array)

    def removeAt(self, index):
        if index < 0:
            pass
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


if __name__ == "__main__":
    array = Array(3)
    array.insert(10)
    array.insert(20)
    array.insert(30)
    array.insert(40)
    array.removeAt(1)
    print(array.indexOf(400))
