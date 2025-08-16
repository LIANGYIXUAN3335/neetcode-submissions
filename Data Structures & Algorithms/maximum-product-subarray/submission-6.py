class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxDp = nums.copy()
        minDp = nums.copy()
        for i in range(1,len(nums)):
            curList = [nums[i], minDp[i - 1] * nums[i],maxDp[i - 1] * nums[i]]
            minDp[i] = min(curList)
            maxDp[i] = max(curList)
        return max(maxDp)
        