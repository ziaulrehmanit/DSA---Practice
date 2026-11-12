class ArrayQueue:
    def __init__(self):
        self.queue = []
        self.start = self.end = -1

    def push(self, x):
        self.queue.append(x)
        if self.start == -1:
            self.start = len(self.queue) - 1
            self.end = len(self.queue) - 1
        else:
            self.end += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError("Invalid Index!")
        val = self.queue[self.start]
        if self.start == self.end:
            self.start = self.end = -1
        else:
            self.start += 1
        return val

    def peek(self):
        if self.isEmpty():
            raise IndexError("Invalid Index!")
        return self.queue[self.start]

    def isEmpty(self):
        return self.start == -1
