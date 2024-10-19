class Stack:
    def __init__(self, initial_values=None, max_size=None):
        if isinstance(initial_values, list):
            self.stack = initial_values
        else:
            self.stack = [initial_values]
        self.max_size = max_size
        self.size = len(self.stack)

    def push(self, value):
        if self.max_size:
            if self.size < self.max_size:
                stack.append(value)
                self.size += 1
            else:
                raise ValueError("The stack is full!")
        else:
            self.stack.append(value)
            self.size += 1

    def top(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def pop(self):
        if self.size > 0:
            if self.stack.pop():
                self.size -= 1
                return True
        return False

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def __len__(self):
        return self.size

    def __str__(self):
        return f"{self.stack}"


if __name__ == "__main__":
    stack = Stack(["Steve", "Jane", "Jim"])
    stack.push("Alice")
    stack.push("bob")
    print(stack, "\n")

    print(stack.pop())
    print(stack, "\n")
    print(stack.pop())
    print(stack, "\n")

    while len(stack) > 0:
        stack.pop()
    if len(stack) == 0:
        print("Stack is empty.")
