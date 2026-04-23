class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # solution 1
        self.res = []
        candidates.sort()
        def dfs(index,curRes,total):
            if total == target:
                self.res.append(curRes.copy())
                return
            for i in range(index,len(candidates)):
                if i >= len(candidates) or total + candidates[i] > target:
                    return
                if i > index and candidates[i] == candidates[i -1]:
                    continue
                curRes.append(candidates[i])
                dfs(i + 1, curRes,total + candidates[i])
                curRes.pop()
        dfs(0,[],0)
        return self.res