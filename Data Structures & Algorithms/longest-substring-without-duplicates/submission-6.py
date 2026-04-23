class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subStringMap = {}
        l = 0
        maxLength = 0
        for r in range(len(s)):
            if s[r] in subStringMap.keys():
                l = max(l, subStringMap[s[r]] + 1)
            maxLength = max(r-l +1, maxLength)
            subStringMap[s[r]] = r
        return maxLength

        