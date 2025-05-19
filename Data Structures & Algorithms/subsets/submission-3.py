class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtracking(start : int, curPath : List[int]) -> None:
            if start == n:
                res.append(curPath.copy())
                return
            backtracking(start + 1, curPath)
            curPath.append(nums[start])
            backtracking(start + 1 , curPath)
            curPath.pop()
        backtracking(0, [])
        return res

        