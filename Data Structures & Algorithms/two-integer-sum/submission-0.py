class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsSet = set(nums)
        for i in range(len(nums)):
            if (target-nums[i]) in numsSet:
                for j in range(i +1 , len(nums)):
                    if nums[j] == target - nums[i]:
                        return [i,j]
        