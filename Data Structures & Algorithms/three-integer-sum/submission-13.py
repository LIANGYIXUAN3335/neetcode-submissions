class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #solution 1 brute force
        # sort nums
        # iterate throght the list get nums[i]
        #   iterate throught the list get nums[j]
        #   if add tuple(nums[i],nums[j],nums[k]) to res
        #       
        # return res
        # nums.sort()
        # res = set()
        # for i in range(len(nums)):
        #     if nums[i] > 0:
        #         break
        #     for j in range(i+1,len(nums)):
        #         target = -nums[i] - nums[j]
        #         for k in range(j +1,len(nums)):
        #             if target == nums[k] :
        #                 res.add(tuple([nums[i],nums[j],nums[k]]))
        #             elif target < nums[k]:
        #                 break
        # return [list(i) for i in res]
        #solution 2 hash map
        # [-4,-1,-1,0,1,2]
        # [-1,-1,2][-1,0,1]
        # nums.sort()
        # res = []
        # count = defaultdict(int)
        # for i in nums:
        #     count[i] += 1
        # for i in range(len(nums)):
        #     count[nums[i]] -= 1
        #     if (i and nums[i] == nums[i-1]):
        #         continue
        #     if nums[i] >0 :
        #         break
        #     for j in range(i+1,len(nums)):
        #         count[nums[j]] -= 1
        #         if (j > i+1 and nums[j] == nums[j-1]):
        #             continue
        #         target = -nums[i]- nums[j]
        #         if count[target] >0:
        #             res.append([nums[i],nums[j],target])
        #     for k in range(i +1,len(nums)):
        #         count[nums[k]] += 1
        # return res
        # solution 3 two pointer
        # [-4,-1,-1,0,1,2]
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] >0:
                break
            if i and nums[i] == nums[i -1]:
                continue
            left , right = i+1, len(nums) -1
            while left < right:
                curSum = nums[left] + nums[right] + nums[i]
                if curSum > 0:
                    right -= 1
                elif curSum <0:
                    left += 1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    right -= 1
                    left += 1
                    while left < len(nums) and nums[left] == nums[left-1]:
                        left += 1
        return res

                
