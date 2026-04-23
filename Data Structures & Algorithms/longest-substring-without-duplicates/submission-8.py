class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        l = 0
        subStringMap = {}
        for r in range(len(s)):
            if s[r] in subStringMap:
                l = max(l,subStringMap[s[r]] + 1)
            subStringMap[s[r]] = r
            maxLength = max(r - l + 1 , maxLength)
        return maxLength
        