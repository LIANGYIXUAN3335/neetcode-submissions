class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0

        for i in range(32):
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1

            total = bit_a ^ bit_b ^ carry
            carry = (bit_a & bit_b) | (bit_a & carry) | (bit_b & carry)

            if total:
                res |= 1 << i

        if res >= 2**31:
            res -= 2**32

        return res