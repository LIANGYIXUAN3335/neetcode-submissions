class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1st solution brute force
        # iterate elements in nums 
            # for each element iterate elements in nums get the multiplier value
        # time complexity O(n^2) space complexity O(n)
        res = [0] * len(nums)
        for i in range(len(nums)):
            initialVal = 1
            for j in range(len(nums)):
                if i ==j :
                    continue
                else:
                    initialVal *= nums[j]
            res[i] = initialVal
        return res



        