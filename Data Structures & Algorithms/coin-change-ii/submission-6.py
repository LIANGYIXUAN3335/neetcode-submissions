class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = 0
        n = len(coins)
        memo = [[-1] * (amount + 1)  for _ in range(len(coins))]
        def dfs(curIndex, curSum):
            if memo[curIndex][curSum] != -1:
                return memo[curIndex][curSum]
            if curSum == 0:
                memo[curIndex][curSum] = 1
                return 1
            res = 0
            for i in range(curIndex, n):
                if curSum - coins[i] < 0:
                    continue
                res += dfs(i, curSum - coins[i])
            memo[curIndex][curSum] = res
            return res
        dfs(0, amount)
        return memo[0][amount]
        
        