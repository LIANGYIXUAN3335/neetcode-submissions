class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1,n + 1):
            cur = i
            curRes = 0
            while cur:
                cur &= cur -1
                curRes += 1
            res[i] = curRes
        return res


        