class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] > nums[0]:
                left = mid + 1
            elif nums[mid] < nums[0]:
                right = mid - 1
            else:
                return min(nums)
        return nums[left]
        