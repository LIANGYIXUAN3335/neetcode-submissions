# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = 0
        def helper( root : Optional[TreeNode]) -> int:
            if not root:
                return 0
            leftHeight = helper(root.left)
            rightHeight = helper(root.right)
            self.res = max(leftHeight + rightHeight , self.res)
            return max(leftHeight, rightHeight) + 1
        helper(root)
        return self.res
            
        