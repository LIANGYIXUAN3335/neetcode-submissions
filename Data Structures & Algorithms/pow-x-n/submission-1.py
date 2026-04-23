class Solution:
    def myPow(self, x: float, n: int) -> float:
        # solution 1 iteration
        # res = 1
        # power = abs(n)
        # while power:
        #     if power & 1:
        #         res *= x
        #     x *=  x
        #     power = power // 2
        # return res if n >0 else 1/res
        # solution 2 recursion
        def helper(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = x if (n % 2) else 1
            return res * helper(x * x, n//2)
        return helper(x,abs(n)) if n > 0 else 1 / helper(x,abs(n))
