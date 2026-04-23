class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = [0]* (n)
        mem[0] = 1
        for i in range(m):
            for j in range(n - 1):
                mem[j+1] = mem[j] + mem[j + 1]

        return mem[-1]