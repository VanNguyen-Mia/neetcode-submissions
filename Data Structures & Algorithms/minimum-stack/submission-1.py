class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    # Pushes the element val onto the stack
    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(min_val)

    # Removes the element on the top of the stack
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    # Gets the top element of the stack
    def top(self) -> int:
        return self.stack[-1]

    # Retrieves the minimum element in the stack
    def getMin(self) -> int:
        return self.minStack[-1]
