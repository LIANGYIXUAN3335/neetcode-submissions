class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def dfs(curList,curSet):
            if len(curSet) == 0:
                self.res.append(curList.copy())
                return
            for i in list(curSet):
                curList.append(i)
                curSet.remove(i)
                dfs(curList,curSet)
                curList.pop()
                curSet.add(i)
        dfs([],set(nums))
        return self.res
        