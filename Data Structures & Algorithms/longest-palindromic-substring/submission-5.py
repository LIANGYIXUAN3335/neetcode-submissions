class Solution:
    def longestPalindrome(self, s: str) -> str:
        # resLen = 1
        # start = 0
        # solution 1: two pointer
        # for i in range(len(s)):
        #     l, r = i, i+ 1
        #     curLen = 0
        #     while l >= 0 and r < len(s) and  s[l] ==  s[r]:
        #         curLen += 2
        #         if resLen < curLen:
        #             start = l 
        #             resLen = curLen
        #         l -= 1
        #         r += 1
        # for i in range(len(s)):
        #     l,r = i, i+2
        #     curLen = 1
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         curLen += 2
        #         if resLen < curLen:
        #             start = l 
        #             resLen = curLen
        #         l -= 1
        #         r += 1
        # return s[start: start+ resLen]
        # solution 2:dp
        resLen = 1
        start = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]        
        for left in range(n - 1, -1, -1):
            for right in range(left, n):
                if s[right] == s[left] and (right - left <= 2 or dp[left + 1][right -1]):
                    dp[left][right] = True
                    curLen = right - left + 1
                    if curLen > resLen:
                        start = left
                        resLen = curLen
        return s[start: start+resLen]



        