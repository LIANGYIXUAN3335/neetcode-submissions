class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[i] == -1:
                    break
                if nums[i] >= n :
                    nums[i] = -1
                    break
                else:
                    temp = nums[nums[i]]
                    nums[nums[i]] = nums[i]
                    nums[i] = temp
        for i in range(n):
            if nums[i] == -1:
                return i
        return n
            

        