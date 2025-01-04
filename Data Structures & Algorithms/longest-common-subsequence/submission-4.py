class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # solution1
        # m = len(text1)
        # n = len(text2)
        # dp = [[0] * (n + 1) for _ in range(m + 1)]
        # for i in range(m):
        #     for j in range(n):
        #         if text1[i] == text2[j]:
        #             dp[i+1][j+1] = dp[i][j] + 1 
        #         else:
        #             dp[i+1][j+1] = max(dp[i][j + 1], dp[i + 1][j])
        # return dp[-1][-1]
        # solution 2
        m = len(text1)
        n = len(text2)
        dp = [0] * (n + 1)
        for i in range(m):
            pre = 0
            for j in range(n):
                cur = dp[j+1]
                if text1[i] == text2[j]:
                    dp[j+1] = pre + 1 
                else:
                    dp[j+1] = max(dp[j + 1], dp[j])
                pre = cur
        return dp[-1]
