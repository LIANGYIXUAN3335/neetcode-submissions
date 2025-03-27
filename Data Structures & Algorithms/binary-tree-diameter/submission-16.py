# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = 0
        
        def helper( root : Optional[TreeNode]) -> [int]:
            if not root:
                return [0,0]
            leftHeight = max(helper(root.left)) + 1
            rightHeight = max(helper(root.right)) + 1
            self.res = max(leftHeight + rightHeight - 2, self.res)
            return [leftHeight, rightHeight]
        helper(root)
        return self.res
            
        