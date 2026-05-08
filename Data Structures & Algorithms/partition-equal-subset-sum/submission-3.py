class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 ==1:
            return False
        target = total //2
        self.res = False
        n = len(nums)
        numSet= set(nums)
        memo = [[False] * n for _ in range(target + 1)]
        for i in range(n):
            memo[0][i] = True
        for index in range(n):
            for total in range(1, target + 1):
                if index == 0:
                    memo[total][index] = total in numSet
                memo[total][index] = memo[total][index - 1] or memo[total - nums[index]][index - 1]
                if memo[total][index] and total == target:
                    return True
        
        return False
        