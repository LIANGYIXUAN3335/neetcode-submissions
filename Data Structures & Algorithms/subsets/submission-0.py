class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # solution 1 backtrackking
        res = []
        curList = []
        n = len(nums)
        def backtracking(i):
            if i >= n:
                res.append(curList.copy())
                return 
            curList.append(nums[i])
            backtracking(i + 1)
            curList.pop()
            backtracking(i + 1)
        backtracking(0)
        return res

        # solution 2

        # solution 3
        