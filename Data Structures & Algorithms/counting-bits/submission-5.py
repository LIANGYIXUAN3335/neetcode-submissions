class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        res = [0] * (n + 1)
        res[1] = 1
        curPos = offset = 2
        while curPos  <= n :
            for i in range(offset):
                res[i + offset] = res[i] + 1
                if i + offset >= n:
                    break
            offset = curPos= 2* offset
        return res