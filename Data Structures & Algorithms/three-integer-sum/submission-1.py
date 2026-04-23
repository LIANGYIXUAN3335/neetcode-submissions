class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # solution 1 brute force 
        # time complexity: O(n^3) space complexity O(n^2)
        res = []
        resSet = set()
        for i in range(len(nums)):
            for j in range(i+ 1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j]+ nums[k] == 0:
                        curRes = [nums[i],nums[j],nums[k]]
                        if tuple(sorted([nums[i],nums[j],nums[k]])) in resSet:
                            continue
                        else:
                            resSet.add(tuple(sorted([nums[i],nums[j],nums[k]])))
                            res.append(curRes)
        return res


