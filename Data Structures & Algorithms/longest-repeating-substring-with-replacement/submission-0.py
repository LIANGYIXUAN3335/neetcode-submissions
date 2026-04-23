class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = [0] * 26
        left = 0
        maxLength = 0
        for right in range(len(s)):
            charCount[ord(s[right]) - ord('A')] += 1
            while (right - left - max(charCount) + 1) > k:
                charCount[ord(s[left]) -  ord('A')] -= 1
                left += 1
            maxLength = max(maxLength,right - left + 1)
        return maxLength


        