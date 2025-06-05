class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        memo = [[False] * n for _  in range(n)]
        for i in range(n):
            memo[i][i] = True
        for start in range(n - 2,  -1, -1):
            for end in range(start + 1, n):
                if s[start] == s[end]:
                    if end - start <= 1:
                        memo[start][end] = True
                    else:
                        memo[start][end] = memo[start + 1][end - 1]
        res = []
        def dfs(startIndex : int,curPath: List[int]):
            if startIndex == n:
                res.append(curPath.copy())
                return
            for end in range(startIndex, n):
                if memo[startIndex][end] :
                    curPath.append(s[startIndex: end + 1])
                    dfs(end + 1, curPath)
                    curPath.pop()
        dfs(0, [])
        return res
    
        