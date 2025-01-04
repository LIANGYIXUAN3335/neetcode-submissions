class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        left, right = 1, len(nums) -1
        for i in range(0,len(nums) -2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  
            left, right = i+ 1, len(nums) -1
            while left < right:
                if left > i +1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue
                curSum = nums[left]+ nums[right] + nums[i]
                if curSum < 0:
                    left += 1
                elif curSum > 0:
                    right -= 1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return res

 
        