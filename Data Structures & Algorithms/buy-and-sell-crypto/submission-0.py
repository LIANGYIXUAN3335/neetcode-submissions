class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers
        left, right = 0,0
        maxProfit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                maxProfit = max(maxProfit, prices[right] - prices[left])
            else:
                left = right
            right +=1
        return maxProfit
        