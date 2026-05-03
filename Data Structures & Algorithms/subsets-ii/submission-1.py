class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        def backtracking(index : int,curPath : List[int]) -> None:
            res.append(curPath.copy())
            for i in range(index, n):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                curPath.append(nums[i])
                backtracking(i + 1, curPath)
                curPath.pop()
        backtracking(0,[])
        return res
        