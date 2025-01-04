class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for i in nums:
            if i not in numSet:
                numSet.add(i)
            else:
                return True
        return False
        
        
        