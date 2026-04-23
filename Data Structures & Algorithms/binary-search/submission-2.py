class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left ,right = 0, len(nums) - 1
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        while left < right -1:
            mid = (left + right) //  2
            if nums[mid] > target:
                right = mid
            elif nums[mid] == target :
                return mid
            else:
                left = mid
        return -1
        