class Solution:
    def longestPalindrome(self, s: str) -> str:
        resL, resR = 0, 0
        n = len(s)
        def expand(l, r):
            nonlocal resL, resR
            if r < n and s[l] == s[r]:
                while l >= 0 and r < n and s[l] == s[r]:
                    
                    l -= 1
                    r += 1
                if resR - resL < r - l - 1:
                    resL = l + 1
                    resR = r 
        for i in range(n):
            expand(i, i)
            expand(i, i + 1)
        return s[resL : resR]

        