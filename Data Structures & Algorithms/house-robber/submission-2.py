class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        maxTotalVal = [0] * n
        maxTotalVal[0] = nums[0]
        maxTotalVal[1] = max(nums[0],nums[1])
        maxVal = max
        for i in range(2,n):
            maxTotalVal[i] = max(nums[i] + maxTotalVal[i-2], maxTotalVal[i-1])
        return max(maxTotalVal[-1],maxTotalVal[-2])



        