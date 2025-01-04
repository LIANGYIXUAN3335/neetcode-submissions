class Solution:
    def countSubstrings(self, s: str) -> int:
        resCount = 0
        # odd substring count
        # for i in range(len(s)):
        #     l, r = i ,i
        #     while l >=0 and r < len(s) and s[l] == s[r]:
        #         resCount += 1
        #         l -= 1
        #         r += 1
            
        # for j in range(len(s) - 1):
        #     l, r = j ,j + 1
        #     while l >=0 and r < len(s) and s[l] == s[r]:
        #         resCount += 1
        #         l -= 1
        #         r += 1
        # return resCount
        # solution 2 dp[][]
        n = len(s)
        resCount = 0
        dp = [[False] * n for _ in range(n)]
        for left in range(n, -1, -1):
            for right in range(left,n):
                if s[left] == s[right] and (right - left <= 2 or dp[left + 1][right - 1]):
                    resCount += 1
                    dp[left][right] =True

        return resCount

        