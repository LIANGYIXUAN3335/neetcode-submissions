class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost)
        memo = [0] * len(cost)
        memo[0] = cost[0]
        memo[1] = cost[1]
        for i in range(2, len(cost)):
            memo[i] = min(memo[i - 1], memo[i - 2]) + cost[i]
        return min(memo[-1], memo[-2])

        