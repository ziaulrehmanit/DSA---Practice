class myQueue:
    def __init__(self, n):
        self.n = n
        self.queue = [None] * n
        self.start = self.end = -1

    def isEmpty(self):
        return self.start == -1

    def isFull(self):
        return (self.end + 1) % self.n == self.start

    def enqueue(self, x):
        if self.isFull():
            return False  # Return False instead of crashing if full

        if self.isEmpty():
            self.start = 0

        ind = (self.end + 1) % self.n
        self.queue[ind] = x
        self.end = ind
        return True

    def dequeue(self):
        if self.isEmpty():
            return -1  # Return -1 instead of crashing if empty

        val = self.queue[self.start]

        if self.start == self.end:
            self.start = self.end = -1
        else:
            self.start = (self.start + 1) % self.n

        return val

    def getFront(self):
        if self.isEmpty():
            return -1  # Return -1 instead of crashing if empty
        return self.queue[self.start]

    def getRear(self):
        if self.isEmpty():
            return -1  # Return -1 instead of crashing if empty
        return self.queue[self.end]
