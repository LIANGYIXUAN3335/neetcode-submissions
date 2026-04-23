class Solution:
    def hammingWeight(self, n: int) -> int:
        # solution1
        # res = 0
        # for i in range(32):
        #     if (1 << i) & n :
        #         res += 1
        # return res
        # solution 2
        # for i in range(32):
        #     if n >> i & 1 :
        #         res += 1
        # return res
        # solution 3
        # res = 0
        # while n:
        #     n &= (n -1)
        #     res += 1
        # return res
        # solution 4
        return bin(n).count('1')

        