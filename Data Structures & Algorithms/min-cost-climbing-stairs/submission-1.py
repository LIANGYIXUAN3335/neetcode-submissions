class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # solution 1 -- dp
        n = len(cost)
        # minCost = [ 0] * (n+1)
        # for i in range(2,n+1):
        #     minCost[i] = min(minCost[i - 1] + cost[i-1] ,minCost[i -2] + cost[i-2])
        # return minCost[n]
        # solution 2 recursive dp
        dp = [-1] * (n+1)
        def recursiveDp(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            else:
                dp[i] = min(recursiveDp(i+1) + cost[i], recursiveDp(i+2) + cost[i])
                return min(recursiveDp(i+1) + cost[i], recursiveDp(i+2)+ cost[i])
        return min(recursiveDp(0) ,recursiveDp(1))