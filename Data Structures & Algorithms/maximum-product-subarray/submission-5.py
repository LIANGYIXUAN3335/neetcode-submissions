class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxDp = nums.copy()
        minDp = nums.copy()
        for i in range(1,len(nums)):
            minDp[i] = min(nums[i], minDp[i - 1] * nums[i],maxDp[i - 1] * nums[i])
            maxDp[i] = max(nums[i], maxDp[i - 1] * nums[i], minDp[i - 1] * nums[i])
        return max(maxDp)
        