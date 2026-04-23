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
        # self.res = []
        # def dfs(curList,used):
        #     if len(curList) == len(used):
        #         self.res.append(curList.copy())
        #         return
        #     for i in range(len(used)):
        #         if used[i]:
        #             continue
        #         curList.append(nums[i])
        #         used[i] = True
        #         dfs(curList,used)
        #         curList.pop()
        #         used[i] = False
        # used = [False] * len(nums)
        # dfs([],used)
        # return self.res
        # solution3
        # self.res = []
        # def dfs(curList,used):
        #     if len(curList) == len(nums):
        #         self.res.append(curList.copy())
        #         return
        #     for i in range(len(nums)):
        #         if not used & 1 << i :
        #             curList.append(nums[i])
        #             dfs(curList, used | (1 << i) )
        #             curList.pop()
        # dfs([],0)
        # return self.res
        # solution 4
        self.res = []
        def dfs(curList,idx):
            if idx == len(nums) - 1:
                self.res.append(curList.copy())
                return
            for i in range(idx , len(nums)):
                nums[idx] , nums[i] = nums[i] , nums[idx]
                dfs(curList, idx +1 )
                nums[i] , nums[idx] = nums[idx] , nums[i]

        dfs(nums,0)
        return self.res

        
        