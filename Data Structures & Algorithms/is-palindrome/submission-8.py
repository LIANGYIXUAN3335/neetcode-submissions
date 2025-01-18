class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, len(s) - 1
        while left < right:
            while left < n and  not s[left].isalnum():
                left += 1
            while right >= 0 and not s[right].isalnum():
                right -= 1
            if left < n and right >= 0 :
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False
        return True
        