class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.leftParenthesis = 0
        self.rightParenthesis = 0
        res = []
        def backtracking(curPath : List[str]) -> None:
            if self.leftParenthesis == n and self.rightParenthesis == n:
                res.append(('').join(curPath))
                return
            if self.leftParenthesis < n:
                curPath.append('(')
                self.leftParenthesis  += 1
                backtracking(curPath)
                curPath.pop()
                self.leftParenthesis -=1
            if self.leftParenthesis > self.rightParenthesis:
                curPath.append(')')
                self.rightParenthesis  += 1
                backtracking(curPath)
                curPath.pop()
                self.rightParenthesis -=1
            
        backtracking([])
        return res
            