class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 1
        start = 0
        # solution 1: two pointer
        for i in range(len(s)):
            l, r = i, i+ 1
            curLen = 0
            while l >= 0 and r < len(s):
                if s[l] ==  s[r]:
                    curLen += 2
                    if resLen < curLen:
                        start = l 
                        resLen = curLen
                    l -= 1
                    r += 1
                else:
                    break
        for i in range(len(s)):
            l,r = i, i+2
            curLen = 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    curLen += 2
                    if resLen < curLen:
                        start = l 
                        resLen = curLen
                    l -= 1
                    r += 1
                else:
                    break

        return s[start: start+ resLen]
                    
            



        # solution 2:dp
        