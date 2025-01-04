class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        def getMaxRob(nums:List[int]) -> int:
            rob1,rob2 = 0,0
            for num in nums:
                newRob = max(rob1+num,rob2)
                rob1 = rob2
                rob2 = newRob
            return rob2
        return max(getMaxRob(nums[:-1]),getMaxRob(nums[1:]))
            
            
        