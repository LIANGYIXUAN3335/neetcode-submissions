class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        dpStart,dpEnd = [0] * (len(nums)),[0] * (len(nums))
        dpStart[0] = nums[0]
        dpStart[1] = max(nums[0],nums[1])
        dpEnd[-1] = nums[-1]
        dpEnd[-2] = max(nums[-1],nums[-2])
        for i in range(2,len(nums) - 1):
            dpStart[i] = max(dpStart[i-1],dpStart[i-2] + nums[i])
        for j in range(n - 3, 0 - 1, -1):  
            dpEnd[j] = max(dpEnd[j + 1], dpEnd[j + 2] + nums[j])
        return max(dpStart[n - 2], dpEnd[1])