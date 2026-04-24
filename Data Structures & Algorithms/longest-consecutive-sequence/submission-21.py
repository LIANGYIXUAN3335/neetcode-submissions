class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for i in numSet:
            if i - 1 in numSet:
                continue
            curRes = 1
            while i + 1 in numSet:
                i += 1
                curRes += 1
            res = max(curRes, res)
        return res
        