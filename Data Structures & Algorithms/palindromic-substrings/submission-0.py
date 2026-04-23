class Solution:
    def countSubstrings(self, s: str) -> int:
        resCount = 0
        # odd substring count
        for i in range(len(s)):
            l, r = i ,i
            while l >=0 and r < len(s) and s[l] == s[r]:
                resCount += 1
                l -= 1
                r += 1
            
        for j in range(len(s) - 1):
            l, r = j ,j + 1
            while l >=0 and r < len(s) and s[l] == s[r]:
                resCount += 1
                l -= 1
                r += 1
        return resCount

        