class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = set()
        res = []
        n = len(nums)
        def backtracking(curPath: List[int]) -> None:
            if len(used) == n:
                res.append(curPath.copy())
                return
            for i in range(n):
                if nums[i] in used:
                    continue
                curPath.append(nums[i])
                used.add(nums[i])
                backtracking(curPath)
                used.remove(nums[i])
                curPath.pop()
        backtracking([])
        return res