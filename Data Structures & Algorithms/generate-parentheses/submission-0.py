class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [ ]
        rightP = 0
        curRes = []
        def backtracking(curN, rightP):
            if curN == 0 and rightP == 0:
                res.append(''.join(curRes))
                return 
            if curN > 0:
                curRes.append('(')
                backtracking(curN -1 , rightP + 1)
                curRes.pop()
            if rightP > 0:
                curRes.append(')')
                backtracking(curN , rightP -1)
                curRes.pop()
        backtracking(n , 0)
        return res
        
        