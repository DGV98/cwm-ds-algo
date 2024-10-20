def balance(str):
    mappings = {
        ")": "(",
        "}": "{",
        "]": "[",
        ">": "<"
    }
    stack = []
    for i in str:
        if i in mappings.values():
            stack.append(i)
        elif i in mappings:
            if not stack:
                return False
            val = stack.pop()
            if val != mappings[i]:
                return False
    return True


if __name__ == "__main__":
    print(balance("((())"))
    print(balance("((())))"))
    print(balance("((()])"))
    print(balance("((()]}))"))
    print(balance("[((()))]"))
