# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        def helper(root:Optional[TreeNode],maxVal : int, minVal :int) -> None:
            if not root or not self.res:
                return 
            if root.val <= minVal or root.val >= maxVal:
                self.res = False
            if root.left and self.res:
                helper(root.left, root.val, minVal)
            if root.right and self.res:
                helper(root.right, maxVal, root.val)
        helper(root,1001, -1001)
        return self.res            
        