class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #solution 1 brute force
        # sort nums
        # iterate throght the list get nums[i]
        #   iterate throught the list get nums[j]
        #   if add tuple(nums[i],nums[j],nums[k]) to res
        #       
        # return res
        nums.sort()
        res = set()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            for j in range(i+1,len(nums)):
                target = -nums[i] - nums[j]
                for k in range(j +1,len(nums)):
                    if target == nums[k] :
                        res.add(tuple([nums[i],nums[j],nums[k]]))
                    elif target < nums[k]:
                        break
        return [list(i) for i in res]
        