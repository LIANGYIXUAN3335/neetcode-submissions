class Solution:
    def reverse(self, x: int) -> int:
        # origin = x
        # x = abs(x)
        # res = int(str(x)[::-1])
        # if origin < 0:
        #     res *= -1
        # if res > (1 << 31 - 1) or res < -(1 <<31):
        #     return 0
        # else:
        #     return res
        def recursion(res : int,x:int) -> int:
            if (x // 10 ==0):
                return res + x%10
            res += x % 10
            res *= 10
            return recursion(res,x // 10 )
        res =  recursion(0,abs(x))
        print(res)
        if x <0:
            res *= -1
        if res < -(1<< 31) or res > (1 << 31 - 1):
            return 0
        return res
        

        