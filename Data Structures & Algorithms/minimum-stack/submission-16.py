class MinStack:

    def __init__(self):
        self.minDiffStack = []
        self.minVal = float('inf')
        

    def push(self, val: int) -> None:
        if len(self.minDiffStack) == 0:
            self.minDiffStack.append(0)
        else:
            self.minDiffStack.append(val - self.minVal)
        if val < self.minVal:
            self.minVal = val

    def pop(self) -> None:
        if len(self.minDiffStack) == 0:
            return
        curDiff = self.minDiffStack.pop()
        if curDiff < 0:
            self.minVal -= curDiff
        if not (self.minDiffStack) :
            self.minVal = float('inf')

    def top(self) -> int:
        curDiff = self.minDiffStack[-1]
        if curDiff >0:
            return curDiff + self.minVal
        else: 
            return self.minVal
        

    def getMin(self) -> int:
        if not self.minDiffStack :
            return None
        return self.minVal
        
