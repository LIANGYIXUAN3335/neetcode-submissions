class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = [0] * 26
        for i in s1:
            s1Map[ord(i) - ord('a')] += 1
        n = len(s1)
        s2Map = [0] * 26
        left, right = 0 , 0
        while right < len(s2):
            s2Map[ord(s2[right]) -  ord('a')] += 1
            right += 1
            if right - left > n:
                s2Map[ord(s2[left]) - ord("a")] -= 1
                left += 1
            if s2Map == s1Map:
                return True
        return False
