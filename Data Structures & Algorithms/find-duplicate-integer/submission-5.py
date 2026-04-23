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
        # for i in nums:
        #     if nums[abs(i)] < 0:
        #         return abs(i)
        #     nums[abs(i)] *= -1
        # return -1
        # solution 4 bit manipulation
        n = len(nums)
        res = 0
        for i in range(32):
            x = y = 0
            b = 1 << i
            for num in nums :
                if num & b :
                    x += 1
            for num in range(1,n):
                if num & b :
                    y += 1
            if x > y:
                res |= b
        return res

        

        