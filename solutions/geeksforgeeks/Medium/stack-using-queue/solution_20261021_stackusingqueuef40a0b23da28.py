from collections import deque

class myStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        # 1. Add to the back of the queue
        self.queue.append(x)
        # 2. Rotate the queue so the new element comes to the front
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        # Return -1 if empty instead of crashing
        if not self.queue:
            return -1
        return self.queue.popleft()

    def top(self):
        # Corrected: peek at the front element or return -1 if empty
        if not self.queue:
            return -1
        return self.queue[0]

    def size(self):
        return len(self.queue)
