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
        # time complexity O(n) space complexity O(n)
        # [1,2,4,6]
        # prefixSum, surfixSum, res = [0] * len(nums),[0] * len(nums),[0] * len(nums)
        # prefixSum[0] = surfixSum[-1] = 1
        # prefixNum = surfixNum = 1
        # for i in range(1,len(nums)):
        #     prefixNum *= nums[i-1]
        #     prefixSum[i] = prefixNum
        # # start stop step
        # for j in range(len(nums)-2,-1,-1):
        #     surfixNum *= nums[j+1]
        #     surfixSum[j] = surfixNum
        # for k in range(len(nums)):
        #     res[k] = prefixSum[k] * surfixSum[k]
        # return res 
        # 3rd solution division operation
        # iterate the nums array - sum
        # nums contains 1 zero
            # 
        # nums contains more than 1 zero
            # res = [0] * len(nums)
        # nums contains 0 zero
            # res = ....
        # time complexity O(n) space complexity O(n)
        numSum = 1
        zeroCount = 0
        for i in nums:
            if i :
                numSum *= i
            else:
                zeroCount += 1
                if zeroCount ==2 :
                    return [0] * len(nums)
        res = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i]:
                if zeroCount ==1:
                    res[i] = 0
                else:
                    res[i] = numSum // nums[i]
            else:
                res[i] = numSum
        return res




        