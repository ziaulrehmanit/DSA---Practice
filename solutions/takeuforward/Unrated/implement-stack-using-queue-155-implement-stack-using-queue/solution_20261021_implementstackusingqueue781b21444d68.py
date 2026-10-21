from collections import deque
class QueueStack:

    def __init__(self):
        # Using a standard deque as our queue
        self.queue = deque()

    def push(self, x: int) -> None:
        # 1. Add to the back of the queue
        self.queue.append(x)
        # 2. Rotate the queue so the new element comes to the front
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        # The front of the queue is the top of the stack
        return self.queue.popleft()

    def top(self) -> int:
        # Peek at the front element
        return self.queue[0]

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

