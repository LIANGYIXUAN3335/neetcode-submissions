class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        n = len(nums)
        for i in range(n ):
            if  i > farthest:
                return False
            farthest = max(nums[i] + i, farthest)
        return True
        