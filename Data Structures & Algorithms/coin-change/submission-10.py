class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # solution 1 top bottom dp
        # memo = {}
        # def helper(amount :int) ->int:
        #     if amount < 0:
        #         return -1
        #     if amount == 0:
        #         return 0
        #     if amount in memo:
        #         return memo[amount]
        #     minVal = float("inf")
        #     for i in coins:
        #         val = helper(amount - i) 
        #         if val == -1:
        #             continue
        #         curVal =val + 1
        #         minVal = min(curVal,minVal)
        #     memo[amount] = -1 if minVal == float("inf") else minVal
        #     return memo[amount]
        # return  helper(amount)
        # solution 2 bottom -up dp
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if (i - coin) >= 0:
                    dp[i] = min(dp[i],dp[i - coin] + 1)
        return -1 if dp[amount] == float('inf') else dp[amount]            
            


        