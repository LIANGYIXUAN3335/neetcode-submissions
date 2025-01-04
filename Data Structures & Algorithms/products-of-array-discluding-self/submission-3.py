class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1st solution brute force
        # iterate elements in nums 
            # for each element iterate elements in nums get the multiplier value
        # time complexity O(n^2) space complexity O(n)
        # res = [0] * len(nums)
        # for i in range(len(nums)):
        #     initialVal = 1
        #     for j in range(len(nums)):
        #         if i ==j :
        #             continue
        #         else:
        #             initialVal *= nums[j]
        #     res[i] = initialVal
        # return res
        # 2nd solution
        # prefix sum array list [1,1,2,8]
        # surfix sum arraylist [48,24,6,1]
        # [1,2,4,6]
        prefixSum, surfixSum, res = [0] * len(nums),[0] * len(nums),[0] * len(nums)
        prefixSum[0] = surfixSum[-1] = 1
        prefixNum = surfixNum = 1
        for i in range(1,len(nums)):
            prefixNum *= nums[i-1]
            prefixSum[i] = prefixNum
        # start stop step
        for j in range(len(nums)-2,-1,-1):
            surfixNum *= nums[j+1]
            surfixSum[j] = surfixNum
        for k in range(len(nums)):
            res[k] = prefixSum[k] * surfixSum[k]
        return res 



        