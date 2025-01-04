class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # solution1 -- bit manipulation
        # res = 0
        # for i in nums:
        #     res = res ^ i
        # return res
        # solution 2 hashset
        numSet = set()
        for i in nums:
            if i in numSet:
                numSet.remove(i)
            else:
                numSet.add(i)
        return numSet.pop()
        # solution 3 -- sorting
        # nums.sort()
        # i = 1
        # while i < len(nums) - 1:
        #     if nums[i - 1] == nums[i]:
        #         i += 2
        #     else:
        #         return nums[i]
        # return 0