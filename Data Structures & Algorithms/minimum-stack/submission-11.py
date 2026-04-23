class MinStack:
    def __init__(self):
        self.minDiffStack = []
        self.minVal = None

    def push(self, val: int) -> None:
        if not self.minDiffStack:
            self.minDiffStack.append(0)
            self.minVal = val
        else:
            self.minDiffStack.append(val - self.minVal)
            if val < self.minVal:
                self.minVal = val

    def pop(self) -> None:
        if not self.minDiffStack:
            return
        diff = self.minDiffStack.pop()
        if diff < 0:
            self.minVal = self.minVal - diff
        if not self.minDiffStack:
            self.minVal = None  # reset for empty case

    def top(self) -> int:
        if not self.minDiffStack:
            return None
        diff = self.minDiffStack[-1]
        if diff >= 0:
            return self.minVal + diff
        else:
            return self.minVal

    def getMin(self) -> int:
        return self.minVal if self.minDiffStack else None