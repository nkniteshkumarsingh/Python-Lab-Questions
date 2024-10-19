from collections import deque


class Queue:
    def __init__(self, initial_values=None, max_size=None):
        self.queue = deque(initial_values)
        self.max_size = max_size
        self.size = len(initial_values)

    def push(self, value):
        if self.max_size:
            if self.size < self.max_size:
                self.queue.append(value)
                self.size += 1
            else:
                raise ValueError("Queue is full!")
        else:
            self.queue.append(value)
            self.size += 1

    def top(self):
        if self.is_empty():
            return None
        else:
            return self.queue[0]

    def pop(self):
        if self.size > 0:
            self.queue.popleft()
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
        return f"{self.queue}"


if __name__ == "__main__":
    queue = Queue(["Steve", "Jane", "Joe"], 6)
    print(len(queue), "\n")

    queue.push("Alice")
    queue.push("Bob")
    queue.push("James")
    # queue.push("Sally")
    print(queue)
    print(len(queue), "\n")

    print(queue.top())
    queue.pop()
    print(queue)
    queue.push("Mallory")
    print(queue)
    print(queue.top(), "\n")

    print(queue)
    while len(queue):
        queue.pop()
