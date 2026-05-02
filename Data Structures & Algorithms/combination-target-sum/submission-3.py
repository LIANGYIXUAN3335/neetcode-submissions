class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtracking(start : int, curPath : List[int], curSum : int):
            if curSum > target or start == n:
                return
            if curSum == target:
                res.append(curPath.copy())
            for i in range(start, n):
                curPath.append(nums[i])
                backtracking(i , curPath, curSum + nums[i])
                curPath.pop()
        backtracking(0, [], 0)
        return res
        