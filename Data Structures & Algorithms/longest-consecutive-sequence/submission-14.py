class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # solution 1 brute force 
        # create set store nums
        # iterate num in nums
        #   while curNum + 1 in set
        #   update maxLength
        # Time complexity O(n^2) space complexity O(n)
        numsSet = set(nums)
        maxLength = 0
        if not nums:
            return 0
        for i in range(len(nums)):
            curNum = nums[i]
            curLength = 1
            while curNum + 1 in numsSet:
                curLength += 1
                curNum += 1
            maxLength = max(maxLength, curLength)
        return maxLength
            



        