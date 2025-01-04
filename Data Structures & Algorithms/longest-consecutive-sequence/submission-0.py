class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #solution 1 
        #brute force 
        #iterate each element in nums and put all nums in one set
        # for each item, if item+1 in set then length + 1 and update the maxmum length
        numSet = set(nums)
        maxLength = 0
        for i in nums:
            curLength = 1
            curNum = i
            while curNum + 1 in numSet:
                curLength +=1
                curNum += 1
            maxLength = max(curLength, maxLength)
        return maxLength
        