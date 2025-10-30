class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = [ -1] *  (n + 1)
        memo[- 1] = 1 
        def df(i):
            if memo[i] != -1:
                return memo[i]
            if s[i] == '0':
                memo[i] = 0
                return 0 
            res = df(i + 1)
            if i < n - 1 and int(s[i : i + 2]) <= 26:
                res += df(i + 2)
            memo[i] = res
            return res
        df(0)
        return memo[0]
        


        