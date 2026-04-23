class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # solution there are 2 state- buying and selling
        # when buying, we reduce the current value with current price 
        # when selling, the next time we can transaction is i + 2 and profit + current price
        dp = {}
        n = len(prices)
        def dfs(index, buying):
            if index >= n:
                return 0
            if (index, buying) in dp:
                return dp[(index, buying)]
            cooldown = dfs(index + 1, buying)
            if buying:
                buy = dfs(index + 1, not buying) - prices[index]
                res =  max(buy, cooldown)
            else:
                sell = dfs(index + 2, not buying) + prices[index]
                res =  max(sell, cooldown)
            dp[(index, buying)] = res
            return res
        dfs(0, True)
        return dp[(0,True)]


        