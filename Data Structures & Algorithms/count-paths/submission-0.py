class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = [[-1]* n for _ in range(m)]
        def dfs(i: int, j : int) -> int:
            if i == m - 1 and j == n - 1:
                return 1
            if i == m or j == n:
                return 0
            if mem[i][j] != -1:
                return mem[i][j]
            else:
                curVal = dfs(i + 1, j) + dfs(i , j+1)
                mem[i][j] = curVal
                return curVal
        return dfs(0,0)