class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # solution 1: hashset
        # numSet = set()
        # for i in nums:
        #     if i in numSet:
        #         return i
        #     numSet.add(i)
        # solution 2: array
        # numArray = [0] * (len(nums))
        # for i in nums:
        #     if numArray[i]:
        #         return i
        #     numArray[i] = 1
        # solution 3 negative marking
        for i in nums:
            if nums[abs(i)] < 0:
                return abs(i)
            nums[abs(i)] *= -1
        return -1
        

        