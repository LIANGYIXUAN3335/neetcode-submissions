class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [amount + 1] * (amount+1)
        memo[0] = 0
        coins.sort()
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    break
                memo[i] = min(memo[i] , memo[i -  coin] + 1)
        return memo[-1] if memo[-1] != amount + 1 else -1
            

        