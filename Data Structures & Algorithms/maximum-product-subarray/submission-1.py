class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # solution 1
        n = len(nums)
        # numMax = [0] * n
        # numMin = [0] * n
        
        # numMax[0] = nums[0]
        # numMin[0] = nums[0]
        # res = nums[0]
        
        # for i in range(1, n):
        #     numMax[i] = max(nums[i], numMax[i-1] * nums[i], numMin[i-1] * nums[i])
        #     numMin[i] = min(nums[i], numMax[i-1] * nums[i], numMin[i-1] * nums[i])
        #     res = max(res, numMax[i])
        
        # return res
        # solution 2
        prefix = 0
        suffix = 0
        res = nums[0]
        for i in range(n):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[n - i - 1]
            res = max(prefix,suffix,res)
        return res
