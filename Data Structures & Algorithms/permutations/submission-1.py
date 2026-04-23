class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # solution 1
        # self.res = []
        # def dfs(curList,curSet):
        #     if len(curSet) == 0:
        #         self.res.append(curList.copy())
        #         return
        #     for i in list(curSet):
        #         curList.append(i)
        #         curSet.remove(i)
        #         dfs(curList,curSet)
        #         curList.pop()
        #         curSet.add(i)
        # dfs([],set(nums))
        # return self.res
        # solution 2
        self.res = []
        def dfs(curList,used):
            if len(curList) == len(used):
                self.res.append(curList.copy())
                return
            for i in range(len(used)):
                if used[i]:
                    continue
                curList.append(nums[i])
                used[i] = True
                dfs(curList,used)
                curList.pop()
                used[i] = False
        used = [False] * len(nums)
        dfs([],used)
        return self.res
        
        