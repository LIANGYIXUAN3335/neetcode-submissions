class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strDigit = ""
        for i in digits:
            strDigit += str(i)
        digit = int(strDigit) +1
        res = []
        for i in str(digit):
            res.append(i)
        return res    
        