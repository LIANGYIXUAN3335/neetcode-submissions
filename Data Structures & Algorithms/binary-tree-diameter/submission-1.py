# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0  # ✅ 在类作用域中定义一个全局变量

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.maxDiameter = max(self.maxDiameter, left + right)
            return max(left, right) + 1

        dfs(root)
        return self.maxDiameter
        