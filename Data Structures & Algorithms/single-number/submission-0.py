class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # solution1 -- bit manipulation
        res = 0
        for i in nums:
            res = res ^ i
        return res
        # solution 2 -- sorting
        # nums.sort()
        # while i < len(nums) - 1:
        #     while nums[i + 1] == nums[i]:
        #         i += 1
        #     return nums[i]
        # return 0