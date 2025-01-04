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
            leftDep = dfs(root.left)
            rightDep = dfs(root.right)
            if abs(leftDep - rightDep) > 1:
                self.res = False
            return max(leftDep,rightDep) + 1
        dfs(root)
        return self.res