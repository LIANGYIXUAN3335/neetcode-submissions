class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n ==0 :
            return 1
        def fastPow(x, n) -> float:
            if n == 1:
                return x
            subPow = fastPow(x, n // 2)
            if n % 2 == 0:
                return subPow * subPow
            else:
                return subPow * subPow * x
        if n > 0:
            return fastPow(x, n)
        else:
            return 1 / fastPow(x , -n)
                
        