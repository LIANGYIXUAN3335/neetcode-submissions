class Solution:
    def numDecodings(self, s: str) -> int:
        # solution 1 - top bottom dp
        n = len(s)
        # dp = [1] * (n +1)
        # for i in range(n-1,-1,-1):
        #     if s[i] == '0':
        #         dp[i] = 0
        #     else:
        #         dp[i] = dp[i + 1]
        #     if i + 1 < n and (s[i] == '1' or (s[i] == '2' and int(s[i+1]) < 7)):
        #         dp[i] += dp[i+2]
        # return dp[0]
        # solution2 - bottom top dp
        dp = [-1] * (n + 1)
        dp[n] = 1
        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            res = 0
            if int(s[i]) == 0:
                dp[i] == 0
            else:
                res = dfs(i + 1)
            if i + 1 < n and (s[i] == '1' or (s[i] == '2' and int(s[i + 1]) < 7)):
                res += dfs(i+ 2)
            return res
        return dfs(0)
            

        