class MinStack:

    def __init__(self):
        self.stack = []

    # Pushes the element val onto the stack
    def push(self, val: int) -> None:
        self.stack.append(val)

    # Removes the element on the top of the stack
    def pop(self) -> None:
        self.stack.pop()

    # Gets the top element of the stack
    def top(self) -> int:
        return self.stack[-1]

    # Retrieves the minimum element in the stack
    def getMin(self) -> int:
        return min(self.stack)
