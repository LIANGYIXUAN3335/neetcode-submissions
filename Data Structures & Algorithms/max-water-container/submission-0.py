from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            # 当前水的高度取决于短板
            curAmount = min(height[left], height[right]) * (right - left)
            res = max(res, curAmount)

            # 谁短就移动谁
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res