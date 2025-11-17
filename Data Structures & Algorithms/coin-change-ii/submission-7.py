class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = 0
        n = len(coins)
        memo = [[-1] * (amount + 1)  for _ in range(len(coins))]
        def dfs(curIndex, curSum):
            if curSum < 0 or curIndex >= n:
                return 0
            if memo[curIndex][curSum] != -1:
                return memo[curIndex][curSum]
            if curSum == 0:
                memo[curIndex][curSum] = 1
                return 1
            use= dfs(curIndex, curSum - coins[curIndex])
            notUse = dfs(curIndex + 1, curSum)
            memo[curIndex][curSum] = use + notUse
            return memo[curIndex][curSum]
        dfs(0, amount)
        return memo[0][amount]
        
        