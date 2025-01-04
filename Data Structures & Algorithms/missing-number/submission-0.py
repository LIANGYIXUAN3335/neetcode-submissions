class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = (1+len(nums)) * len(nums) /2
        for i in nums:
            res -= i
        return int(res)
        