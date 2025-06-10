class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = {'2' : ['a','b','c'], '3' : ['d','e','f'], '4' : ['g','h','i'],
        '5' : ['j','k','l'] , '6' : ['m', 'n' , 'o'], '7' :['p','q', 'r', 's'],
        '8': ['t','u','v'], '9' :['w','x','y','z']}
        res = []
        n = len(digits)
        if n == 0:
            return res
        def backtracking(index : int, curPath: List[str]) -> None:
            if index == n:
                res.append("".join(curPath))
                return
            for letter in digitMap[digits[index]]:
                curPath.append(letter)
                backtracking(index + 1, curPath)
                curPath.pop()
        backtracking(0, [])
        return res
        