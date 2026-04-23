class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [-1] * n
        def dfs(i):
            if i >= n:
                return i == n
            if mem[i] != -1:
                return mem[i]
            mem[i]=  dfs(i+1) + dfs(i+2)
            return mem[i]
        return dfs(0)
        