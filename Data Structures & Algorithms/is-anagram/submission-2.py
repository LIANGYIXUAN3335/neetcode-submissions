class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chMap = [0] * 26
        if len(s) != len(t):
            return False
        for ch in s:
            chMap[ord(ch) - ord('a')] += 1
        for ch in t:
            chMap[ord(ch) - ord('a')] -= 1
            if chMap[ord(ch) - ord('a')] < 0:
                return False
        return True

        