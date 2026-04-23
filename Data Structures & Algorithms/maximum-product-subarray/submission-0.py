class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        numMax = [0] * n
        numMin = [0] * n
        
        numMax[0] = nums[0]
        numMin[0] = nums[0]
        res = nums[0]
        
        for i in range(1, n):
            numMax[i] = max(nums[i], numMax[i-1] * nums[i], numMin[i-1] * nums[i])
            numMin[i] = min(nums[i], numMax[i-1] * nums[i], numMin[i-1] * nums[i])
            res = max(res, numMax[i])
        
        return res