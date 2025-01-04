class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # solution there are 2 state- buying and selling
        # when buying, we reduce the current value with current price 
        # when selling, the next time we can transaction is i + 2 and profit + current price
        n = len(prices)
        nextBuy, nextSell = 0,0
        next2Buy = 0
        for i in range(n-1,-1,-1):
            curBuy = max(nextSell - prices[i],nextBuy)
            curSell = max(next2Buy + prices[i], nextSell)
            next2Buy = nextBuy
            nextBuy, nextSell = curBuy, curSell
        return curBuy


        