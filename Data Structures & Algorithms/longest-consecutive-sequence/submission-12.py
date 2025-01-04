class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #solution 1 
        #brute force 
        #iterate each element in nums and put all nums in one set
        # for each item, if item+1 in set then length + 1 and update the maxmum length
        # numSet = set(nums)
        # maxLength = 0
        # for i in nums:
        #     curLength = 1
        #     curNum = i
        #     while curNum + 1 in numSet:
        #         curLength +=1
        #         curNum += 1
        #     maxLength = max(curLength, maxLength)
        # return maxLength
        # solution 2 sorting
        if not nums:
            return 0
        maxLength = 1
        nums = list(set(nums))
        nums.sort()
        curLength = 1
        for i in range(0,len(nums)-1):
            if nums[i+1] == nums[i]+1:
                curLength += 1
                maxLength = max(maxLength, curLength)
            else:
                curLength = 1
        return maxLength

        