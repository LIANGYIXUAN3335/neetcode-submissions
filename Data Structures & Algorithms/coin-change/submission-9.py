class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def helper(amount :int) ->int:
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            minVal = float("inf")
            for i in coins:
                val = helper(amount - i) 
                if val == -1:
                    continue
                curVal =val + 1
                minVal = min(curVal,minVal)
            memo[amount] = -1 if minVal == float("inf") else minVal
            return memo[amount]
        return  helper(amount)
            
            


        