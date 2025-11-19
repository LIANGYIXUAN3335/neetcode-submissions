class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for curSum in range(coin, amount + 1):
                dp[curSum] += dp[curSum - coin]
        return dp[-1]
                
