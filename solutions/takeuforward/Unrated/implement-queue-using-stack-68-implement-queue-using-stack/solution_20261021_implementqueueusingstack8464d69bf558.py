class StackQueue:
    
    def __init__(self):
        # Two standard Python lists acting strictly as stacks (only append and pop)
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        # Push onto the main input stack
        self.in_stack.append(x)

    def pop(self) -> int:
        # Move elements to out_stack if it's empty
        self.move_elements()
        return self.out_stack.pop()

    def peek(self) -> int:
        # Move elements to out_stack if it's empty
        self.move_elements()
        return self.out_stack[-1]

    def isEmpty(self) -> bool:
        # The queue is empty only if both stacks are empty
        return not self.in_stack and not self.out_stack

    def move_elements(self) -> None:
        # Helper function to transfer elements when needed
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
