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
        # def recursion(res : int,x:int) -> int:
        #     if (x // 10 ==0):
        #         return res + x%10
        #     res += x % 10
        #     res *= 10
        #     return recursion(res,x // 10 )
        # res =  recursion(0,abs(x))
        # print(res)
        # if x <0:
        #     res *= -1
        # if res < -(1<< 31) or res > (1 << 31 - 1):
        #     return 0
        # return res
        MIN = -(1 << 31)
        MAX = 1 << 31 -1
        res = 0
        while x : 
            digit = int(math.fmod(x,10))
            x = int(x / 10)
            if res < MIN // 10 or (res == MIN // 10 and digit < -8):  
                return 0
            if res > MAX // 10 or (res ==MAX // 10 and digit > 7):
                return 0
            res = res * 10 + digit
        return res
        

        