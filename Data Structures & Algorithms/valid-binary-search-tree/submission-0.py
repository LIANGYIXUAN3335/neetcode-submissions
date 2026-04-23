# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root: Optional[TreeNode],leftBound,rightBound) -> bool:
            if not root:
                return True
            if root.val < rightBound and root.val > leftBound:
                return helper(root.left,leftBound, root.val) and helper(root.right,root.val,rightBound)
            else:
                return False
        leftBound = -float('inf')
        rightBound = float('inf')
        return helper(root,leftBound,rightBound)

        