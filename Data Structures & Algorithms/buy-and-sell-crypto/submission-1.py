class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers
        minBuy = prices[0]
        maxProfit = 0
        for sell in prices:
            maxProfit = max(sell - minBuy, maxProfit)
            minBuy = min(minBuy, sell)
        return maxProfit
        