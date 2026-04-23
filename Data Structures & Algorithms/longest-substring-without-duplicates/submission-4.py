class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subStringMap = {}
        l = 0
        maxLength = 0
        for r in range(len(s)):
            if s[r] in subStringMap:
                l = max(l, subStringMap[s[r]] + 1)
            subStringMap[s[r]] = r
            maxLength = max(maxLength, r - l + 1)
        return maxLength