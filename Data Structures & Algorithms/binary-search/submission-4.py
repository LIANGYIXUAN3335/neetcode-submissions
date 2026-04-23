class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left, right = 0,len(nums)
        # while left < right:
        #     mid = (right - left ) // 2 + left
        #     if nums[mid] > target:
        #         right = mid - 1
        #     elif nums[mid] < target:
        #         left = mid + 1
        #     else:
        #         return mid
        # return -1
        # solution 2
        left,right = 0,len(nums)
        while left < right:
            mid = (right - left ) // 2 + left
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left - 1 if nums[left - 1] == target else -1 
        
        