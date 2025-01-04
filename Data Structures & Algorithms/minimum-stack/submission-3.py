class MinStack:

    def __init__(self):
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.minStack.append(val)

    def pop(self) -> None:
        if self.minStack:
            self.minStack.pop()

    def top(self) -> int:
        top = self.minStack.pop()
        self.minStack.append(top)
        return top
    def getMin(self) -> int:
        if not self.minStack:
            return 0
        return min(self.minStack)
