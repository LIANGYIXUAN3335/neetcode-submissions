class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        def backtracking(curRes : List[int],index:int):
            curSum = sum(curRes)
            print(curSum)
            if curSum == target:
                self.res.append(curRes.copy())
                return
            if curSum > target or index >= len(nums):
                return 
            curRes.append(nums[index])
            backtracking(curRes,index )
            curRes.pop()
            backtracking(curRes,index + 1)
        backtracking([],0)
        return self.res
            
