class myQueue:
    def __init__(self):
        # Use two standard lists as our stacks
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        # Push element onto the first stack
        self.s1.append(x)

    def dequeue(self):
        # If both stacks are empty, nothing to dequeue
        if not self.s1 and not self.s2:
            return
        
        # If s2 is empty, move everything from s1 to s2
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
                
        # Pop the front element from s2
        self.s2.pop()

    def front(self):
        # If both stacks are empty, return -1
        if not self.s1 and not self.s2:
            return -1
            
        # If s2 is empty, move everything from s1 to s2
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
                
        # Peek at the top of s2 (which is the front of the queue)
        return self.s2[-1]

    def size(self):
        # The total size is the sum of elements in both stacks
        return len(self.s1) + len(self.s2)
