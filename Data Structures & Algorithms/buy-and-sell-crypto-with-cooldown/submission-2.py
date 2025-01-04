class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # solution there are 2 state- buying and selling
        # when buying, we reduce the current value with current price 
        # when selling, the next time we can transaction is i + 2 and profit + current price
        n = len(prices)
        buy, sell = [-1] * (n + 1),[-1] * (n + 1)
        def dfs(index, buying):
            if index >= n:
                return 0
            if buying:
                if buy[index] != -1:
                    return buy[index] 
                curbuy = dfs(index + 1, not buying) - prices[index]
                cooldown = dfs(index + 1 , True)
                buy[index]  =  max(curbuy, cooldown)
                return buy[index]
            else:
                if sell[index] != -1:
                    return sell[index] 
                cursell = dfs(index + 2, not buying) + prices[index]
                cooldown = dfs(index + 1 , False)
                sell[index] =  max(cursell, cooldown)
                return sell[index]
        dfs(0, True)
        return buy[0] if buy[0] > 0 else 0


        