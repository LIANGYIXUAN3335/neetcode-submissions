class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # solution there are 2 state- buying and selling
        # when buying, we reduce the current value with current price 
        # when selling, the next time we can transaction is i + 2 and profit + current price
        n = len(prices)
        buy, sell = [0] * (n + 2),[0] * (n + 2)
        for i in range(n-1,-1,-1):
            for j in [True, False]:
                if j :
                    curBuy = sell[i + 1] - prices[i]
                    coolDown = buy[i + 1]
                    buy[i] = max(curBuy,coolDown)
                else:
                    curSell = buy[i + 2] + prices[i]
                    coolDown = sell[i + 1]
                    sell[i] = max(curSell,coolDown)
        return buy[0] 


        