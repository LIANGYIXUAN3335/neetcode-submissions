class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()
        def backtracking(start : int, curPath : List[int], curSum : int):
            if curSum == target:
                res.append(curPath.copy())
                return
            if start == n:
                return
            for i in range(start, n):
                if curSum + candidates[i] > target:
                    continue
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                curPath.append(candidates[i])
                backtracking(i + 1 , curPath, curSum + candidates[i])
                curPath.pop()
        backtracking(0, [], 0)
        return res