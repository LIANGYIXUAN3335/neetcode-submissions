class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        memo = [[False] * n for _ in range(n)] 
        left, right = 0 , 0
        for i in range(n - 1, - 1, - 1):
            for j in range(i, n):
                if i == j:
                    memo[i][j] = True
                elif j == i + 1 and s[i] == s[j]:
                    memo[i][j] = True
                elif j - i >= 2 and s[i] == s[j] and memo[i + 1][j - 1]:
                    memo[i][j] = True
                if memo[i][j] and right - left  < j - i + 1:
                    left = i
                    right = j + 1
        return s[left: right]
        