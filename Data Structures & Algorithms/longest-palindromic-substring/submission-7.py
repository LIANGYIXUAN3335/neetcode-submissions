class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        memo = [[False] * n for _ in range(n)] 
        res = ""
        for i in range(n - 1, - 1, - 1):
            for j in range(i, n):
                if i == j:
                    memo[i][j] = True
                elif j == i + 1 and s[i] == s[j]:
                    memo[i][j] = True
                elif j - i >= 2 and s[i] == s[j] and memo[i + 1][j - 1]:
                    memo[i][j] = True
                if memo[i][j] and len(res) < j - i + 1:
                    res = s[i : j + 1]
        return res
        