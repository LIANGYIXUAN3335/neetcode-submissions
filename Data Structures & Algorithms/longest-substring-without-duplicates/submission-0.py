class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l,r = 0,0
        maxLength = 0
        while l <= r and r < len(s):
            if s[r] not in charSet:
                charSet.add(s[r])
                r += 1
                maxLength = max(r - l , maxLength)
            else:
                charSet.remove(s[l])
                l += 1
        return maxLength

        