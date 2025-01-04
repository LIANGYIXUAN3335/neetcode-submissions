# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        heightMap = {}
        def getMaxHeight(root:Optional[TreeNode]) -> int:
            if not root:
                heightMap[root] = 0
                return 0
            if root in heightMap:
                return heightMap[root]
            else:
                heightMap[root] = max(getMaxHeight(root.left) ,getMaxHeight(root.right)) + 1
                return max(getMaxHeight(root.left) ,getMaxHeight(root.right)) + 1
        heightMap[root] = getMaxHeight(root)
        maxLength = 0
        print(heightMap)
        for root in heightMap:
            if not root:
                continue
            maxLength = max(heightMap[root.left] + heightMap[root.right] , maxLength)
        return maxLength
        
        