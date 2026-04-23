class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # solution 1
        # strDigit = ""
        # for i in digits:
        #     strDigit += str(i)
        # digit = int(strDigit) +1
        # res = []
        # for i in str(digit):
        #     res.append(i)
        # return res    
        # solution 2
        last = int(digits[-1]) + 1
        offset = last // 10
        last = last % 10
        digits[-1] = last
        for i in range(len(digits)-2, -1,-1):
            cur = offset + int(digits[i])
            offset = cur // 10
            cur = cur % 10
            digits[i] = str(cur)
        if offset == 1:
            return [1]+ digits
        else :
            return digits
        
        