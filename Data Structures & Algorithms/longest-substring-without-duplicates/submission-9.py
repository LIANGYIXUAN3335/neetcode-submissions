class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chSet = set()
        left , right = 0,0
        res = 0
        while right < len(s):
            while s[right] in chSet:
                chSet.remove(s[left])
                left += 1
            chSet.add(s[right])
            right += 1
            res = max(res, right - left)
        return res

        