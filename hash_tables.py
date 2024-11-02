def first_non_repeated_char(str):
    mapping = {}
    for char in str:
        if char in mapping:
            mapping[char] += 1
        else:
            mapping[char] = 1
    for char in str:
        if mapping[char] == 1:
            return char
    return "None"


def first_repeated_char(str):
    s = set()
    for char in str:
        if char in s:
            return char
        s.add(char)
    return ""


def count_pairs_with_diff(nums, k):
    # O(n)
    i = 0
    n = len(nums)
    s = set(nums)
    s_pairs = set()
    for num in nums:
        if (num - k) in s:
            s_pairs.add(((num - k), num))
        elif (num + k) in s:
            s_pairs.add((num, (num + k)))
    return len(s_pairs)


def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        if (target - num) in hashmap:
            return [hashmap[target - num], i]
        hashmap[num] = i
    return []


def most_frequent_element(nums):
    hashmap = {}
    for num in nums:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1
    max_el = None
    for num, val in hashmap.items():
        if max_el == None:
            max_el = num
        if val > hashmap[max_el]:
            max_el = num
    return max_el


class Entry:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value


class Node:
    def __init__(self, entry: Entry):
        self.entry = entry
        self.next = None


class HashTable:
    def __init__(self, capacity):
        self.map = [None] * capacity

    def put(self, key, value):
        entry = Entry(key, value)
        node_entry = Node(entry)
        index = self.hash_function(key)
        if not self.map[index]:
            self.map[index] = node_entry
        else:
            node = self.map[index]
            while node.next:
                node = node.next
            node.next = node_entry

    def get(self, key):
        i = self.hash_function(key)
        if not self.map[i]:
            return None
        node = self.map[i]
        while node:
            if node.entry.key == key:
                return node.entry.value
            node = node.next
        return None

    def remove(self, key):
        i = self.hash_function(key)
        if not self.map[i]:
            return
        node = self.map[i]
        if node.entry.key == key:
            self.map[i] = node.next
        else:
            prev = node
            node = node.next
            while node:
                if node.entry.key == key:
                    prev.next = node.next
                prev = node
                node = node.next

    def hash_function(self, key):
        capacity = len(self.map)
        return key % capacity


if __name__ == "__main__":
    # print(first_non_repeated_char('green'))
    # print(first_repeated_char('green'))
    hashmap = HashTable(5)
    hashmap.put(5, "Hello")
    print(hashmap.get(5))
    print(most_frequent_element([1, 1, 1, 2, 2, 4, 4, 4, 4, 5, 6, 7, 7, 7]))
    print(count_pairs_with_diff([1, 7, 5, 9, 2, 12, 3], 2))
    print(two_sum([2, 7, 11, 15], 17))
