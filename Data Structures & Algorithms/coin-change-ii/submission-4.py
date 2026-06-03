class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}

        def dfs(i, remain):
            if remain == 0:
                return 1
            if i == n or remain < 0:
                return 0

            if (i, remain) in memo:
                return memo[(i, remain)]

            # choice 1: use coins[i], stay at same i because unlimited coins
            use_it = dfs(i, remain - coins[i])

            # choice 2: skip coins[i], move to next coin
            skip_it = dfs(i + 1, remain)

            memo[(i, remain)] = use_it + skip_it
            return memo[(i, remain)]

        return dfs(0, amount)