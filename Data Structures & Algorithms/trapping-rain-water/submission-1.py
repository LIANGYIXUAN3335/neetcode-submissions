class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        leftMax = 0
        rightMax = 0
        while left <= right:
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left]) 
                if leftMax  > height[left]:
                    res += leftMax - height[left] 
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                if rightMax > height[right]:
                    res += rightMax - height[right]
                right -= 1
        return res
        