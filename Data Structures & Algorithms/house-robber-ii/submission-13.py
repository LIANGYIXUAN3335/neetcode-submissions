class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0:2])
        def helper(start, end)-> int:
            # if end - start == 0:
            #     return nums[start]
            # if end - start == 1:
            #     return max(nums[start: end + 1])
            n = end - start + 1
            memo = [0] * n
            memo[0] = nums[start]
            memo[1] = max(nums[start:start + 2])
            for i in range(2, n):
                memo[i] = max(nums[start + i] + memo[i - 2] , memo[i - 1])
            return memo[-1]
        return max(helper(0, n - 2),helper(1, n - 1 ))