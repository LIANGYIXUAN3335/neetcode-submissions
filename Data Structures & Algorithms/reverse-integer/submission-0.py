class Solution:
    def reverse(self, x: int) -> int:
        origin = x
        x = abs(x)
        res = int(str(x)[::-1])
        if origin < 0:
            res *= -1
        if res > (1 << 31 - 1) or res < -(1 <<31):
            return 0
        else:
            return res
        
        