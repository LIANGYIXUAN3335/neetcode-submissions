class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        offset = 0
        while n :
            if n % 2:
                res += 1 << (31-offset)
            n = n //2
            offset += 1
        return res
        