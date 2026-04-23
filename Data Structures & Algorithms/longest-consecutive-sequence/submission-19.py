class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0
        for i in nums:
            if i - 1 not in numSet:
                cur = i
                curMax = 1
                while cur + 1 in numSet:
                    curMax += 1
                    cur += 1
                maxLen = max(maxLen,curMax)
        return maxLen
