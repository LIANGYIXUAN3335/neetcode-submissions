class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [[0] * (amount + 1) for _ in range(len(coins))]    
        for curSum in range(amount + 1):
            for index in range(len(coins) - 1 , -1, -1):
                if curSum ==0:
                    dp[index][curSum] = 1
                else:
                    if index < len(coins) - 1:
                        dp[index][curSum] += dp[index + 1][curSum]
                    if curSum - coins[index] >= 0:
                        dp[index][curSum] += dp[index][curSum - coins[index]]
        return dp[0][amount]
