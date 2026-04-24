class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        chMap = [0] * 26
        res = 0
        while right < len(s):
            chMap[ord(s[right]) - ord("A")] += 1
            right += 1
            while right - left - max(chMap) > k:
                chMap[ord(s[left]) - ord("A")] -= 1
                left += 1
            res = max(res, right - left)
        return res

        