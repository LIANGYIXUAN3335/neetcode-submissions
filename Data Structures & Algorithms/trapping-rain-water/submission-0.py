class Solution:
    def trap(self, height: List[int]) -> int:
        leftHeight ,rightHeight = 0,0
        leftIndex,rightIndex = 0, len(height) - 2
        leftHeights = [0] * len(height)
        res = 0
        for i in range(1, len(height)):
            leftHeight = max(leftHeight ,height[i - 1])
            leftHeights[i] = max(leftHeight,height[i - 1])
        leftHeight = 0
        while leftIndex< rightIndex:
            rightHeight = max(rightHeight,height[rightIndex + 1])
            res += max(0,min(rightHeight,leftHeights[rightIndex]) - height[rightIndex])
            rightIndex -=1
        return res

