# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def helper(root:TreeNode, curMax :int) -> None:
            if not root:
                return
            if root.val >= curMax:
                self.res += 1
            curMax = max(curMax,root.val)
            helper(root.left,curMax)
            helper(root.right,curMax)
        helper(root,root.val)
        return self.res
        