class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = dict()
        for right in range(len(nums)):
            if target - nums[right] in numMap:
                return [numMap[target - nums[right]], right]
            numMap[nums[right]] = right
        return []
                