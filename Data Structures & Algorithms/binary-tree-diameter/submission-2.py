# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxLength = 0
        def getMaxDepth(root:Optional[TreeNode]):
            if not root:
                return 0
            leftDepth = getMaxDepth(root.left)
            rightDepth = getMaxDepth(root.right)
            self.maxLength = max(self.maxLength, leftDepth + rightDepth)
            return max(leftDepth,rightDepth) + 1
        getMaxDepth(root)
        return self.maxLength