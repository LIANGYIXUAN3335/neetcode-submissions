class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        def twoSum(start, end, target) -> List[List[int]]:
            res = []
            while start < end:
                curSum =nums[start] + nums[end]
                if curSum == target:
                    res.append([nums[start], nums[end]])
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    while end < start and nums[end] == nums[end - 1]:
                        end -= 1
                    start += 1
                    end -= 1
                elif curSum < target:
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    start += 1
                else:
                    while end > start and nums[end] == nums[end - 1]:
                        end -= 1
                    end -= 1
            return res
                
        for start in range(0,  n - 2):
            if start != 0 and nums[start] == nums[start - 1]:
                continue
            for left, right in twoSum(start + 1, n - 1, 0 - nums[start]):
                res.append([nums[start], left, right])
        return res
        

        