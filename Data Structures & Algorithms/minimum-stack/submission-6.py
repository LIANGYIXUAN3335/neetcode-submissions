class MinStack:

    def __init__(self):
        self.minStack = []
        self.minValueStack = []
        

    def push(self, val: int) -> None:
        self.minStack.append(val)
        if len(self.minValueStack) == 0:
            minVal = val
        else:
            minVal = min(self.minValueStack[-1],val)
        self.minValueStack.append(minVal)

    def pop(self) -> None:
        if self.minStack:
            self.minStack.pop()
            self.minValueStack.pop()

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        return self.minValueStack[-1]
