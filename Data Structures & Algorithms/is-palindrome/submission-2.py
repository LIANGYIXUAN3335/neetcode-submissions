class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0 ,len(s) -1
        while l < r:
            if s[l].isalnum() == False:
                l +=1
            elif s[r].isalnum() ==False:
                r -=1
            elif s[r].lower() != s[l].lower():
                return False
            else:
                r -=1 
                l += 1
        return True

        