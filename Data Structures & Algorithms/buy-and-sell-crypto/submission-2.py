class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float("inf")
        res = 0
        for i in prices:
            res = max(res, i - minPrice)
            minPrice = min(i, minPrice)
        return res

        