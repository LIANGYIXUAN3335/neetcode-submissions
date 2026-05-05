class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        n = len(nums)
        memo = [0] * n
        memo[0] = nums[0]
        memo[1] = max(nums[0:2])
        for i in range(2, n):
            memo[i] = max(nums[i] + memo[i - 2] , memo[i - 1])
        
        return memo[-1]
        