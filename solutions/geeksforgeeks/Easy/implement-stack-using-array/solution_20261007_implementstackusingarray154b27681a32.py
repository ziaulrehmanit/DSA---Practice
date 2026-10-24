class myStack:
    def __init__(self, n: int):
        self.n = n
        self.stack = [0] * n
        self.top = -1
    
    def push(self, x: int) -> None:
        # Note: All queries are guaranteed valid by constraints,
        # but a safety check prevents out-of-bounds just in case.
        if not self.isFull():
            self.top += 1
            self.stack[self.top] = x
    
    def pop(self) -> None:
        if not self.isEmpty():
            self.top -= 1
    
    def peek(self) -> int:
        if self.isEmpty():
            return -1
        return self.stack[self.top]
    
    def isEmpty(self) -> bool:
        return self.top == -1
    
    def isFull(self) -> bool:
        return self.top == self.n - 1
