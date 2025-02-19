import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index =  bisect.bisect_left(nums, target)
        n = len(nums)
        return index  if index < n and nums[index] == target else -1
        