# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -1001
        def helper(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            leftMax = helper(root.left)
            rightMax = helper(root.right)
            curMax = root.val
            if leftMax > 0:
                curMax += leftMax
            if rightMax > 0:
                curMax += rightMax
            self.res = max(self.res ,curMax)
            return max(root.val, root.val + leftMax, root.val + rightMax)
        helper(root)
        return self.res

            
        