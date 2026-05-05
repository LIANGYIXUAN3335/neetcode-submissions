class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        res = digits.copy()
        for i in range(len(res) - 1,  - 1, -1):
            curSum = res[i] + carry
            res[i] = curSum % 10
            carry = curSum // 10
        if carry:
            res = [1] + res
        return res
