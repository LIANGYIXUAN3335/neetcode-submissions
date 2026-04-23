class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # solution 1 backtrackking
        res = []
        n = len(nums)
        def backtracking(i,curList):
            if i >= n:
                res.append(curList.copy())
                return 
            backtracking(i + 1,curList)
            backtracking(i + 1,curList + [nums[i]])
        backtracking(0,[])
        return res

        # solution 2

        # solution 3
        