class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        def backtracking(curRes : List[int],index:int,total :int):
            if total == target:
                self.res.append(curRes.copy())
                return
            if total > target or index >= len(nums):
                return 
            curRes.append(nums[index])
            backtracking(curRes,index,total+ nums[index] )
            curRes.pop()
            backtracking(curRes,index + 1,total)
        backtracking([],0,0)
        return self.res
            
