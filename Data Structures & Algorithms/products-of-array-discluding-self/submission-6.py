class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        curMal = 1
        for i in range(1,len(nums)):
            curMal *= nums[i - 1]
            res[i] *= curMal
        curMal = 1
        for j in range(len(nums) - 2, -1 , - 1):
            curMal *= nums[j + 1]
            res[j] *= curMal
        return res