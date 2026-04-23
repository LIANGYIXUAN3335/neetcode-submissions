class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # solution 1 brute force 
        # create set store nums
        # iterate num in nums
        #   while curNum + 1 in set
        #   update maxLength
        # Time complexity O(n^2) space complexity O(n)
        # numsSet = set(nums)
        # maxLength = 0
        # if not nums:
        #     return 0
        # for i in range(len(nums)):
        #     curNum = nums[i]
        #     curLength = 1
        #     while curNum + 1 in numsSet:
        #         curLength += 1
        #         curNum += 1
        #     maxLength = max(maxLength, curLength)
        # return maxLength

        # solution 2 sort
        # nums deduplicate
        # nums.sort() nlogn
        # iterate nums:
        # nums[i + 1] = nums[i] + 1 
        # curLength += 1
        # timeComplexity : nlogn space complexity o(1)
        # nums = list(set(nums))
        # nums.sort()
        # if not nums:
        #     return 0
        # maxLength = 1
        # curLength = 1
        # for i in range(len(nums)-1):
        #     if nums[i + 1] == nums[i] + 1:
        #         curLength += 1
        #         maxLength = max(maxLength, curLength)
        #     else:
        #         curLength = 1
        # return maxLength
        # solution 3 
        # [2,20,4,10,3,4,5]
        # O(n), O(n)
        numsSet = set(nums)
        maxLength = 1
        if not nums:
            return 0
        for i in range(len(nums)):
            if nums[i] -1 in numsSet:
                continue
            else:
                curLength = 1
                curNum = nums[i]
                while curNum + 1 in numsSet:
                    curLength+= 1
                    curNum += 1
                maxLength = max(maxLength, curLength)
        return maxLength




        