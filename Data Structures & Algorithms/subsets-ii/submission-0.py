class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        n = len(nums)
        nums.sort()
        def dfs(index):
            res.append(cur[:])
            for i in range(index,n):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                cur.append(nums[i])
                dfs(i + 1)
                cur.pop()
        dfs(0)
        return res

        