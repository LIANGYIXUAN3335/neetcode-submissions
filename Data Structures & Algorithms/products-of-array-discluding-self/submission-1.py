class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1st Solution:
        # n = len(nums)
        # res = [] 
        # zero_count = 0
        # for i in range(len(nums)):
        #     curNum = 1
        #     for j in range(len(nums)):
        #         if i == j :
        #             continue
        #         if curNum ==0 :
        #             break
        #         curNum *= nums[j]
        #     res.append(curNum)
        # return res
        # 2nd solution
        # prefix sum and surfix sum
        # iterate for left to right and right to left 
        n = len(nums)
        prefixSum, surfixSum, res = [0] * n,[0] * n,[0] * n
        prefixNum = 1
        surfixNum = 1
        prefixSum[0] = surfixSum[-1] = 1
        for i in range(1,len(nums)):
            prefixNum *= nums[i-1]
            prefixSum[i] = prefixNum
        # start stop step
        for j in range(len(nums) -2 ,-1, -1):
            surfixNum *= nums[j+1]
            surfixSum[j] = surfixNum
        for i in range(len(nums)):
            res[i] = prefixSum[i] * surfixSum[i]
        return res

        