# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            leftHeight = dfs(root.left) + 1
            rightHeight = dfs(root.right) + 1
            if abs(leftHeight - rightHeight) > 1:
                self.res = False
            return max(leftHeight, rightHeight)
        dfs(root)
        return self.res
        