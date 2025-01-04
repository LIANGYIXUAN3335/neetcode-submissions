class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [] 
        zero_count = 0
        for i in range(len(nums)):
            curNum = 1
            for j in range(len(nums)):
                if i == j :
                    continue
                if curNum ==0 :
                    break
                curNum *= nums[j]
            res.append(curNum)
        return res
        