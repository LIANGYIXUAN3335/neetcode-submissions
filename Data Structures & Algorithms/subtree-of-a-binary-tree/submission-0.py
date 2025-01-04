# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # solution1 :
        if subRoot ==None:
            return True
        if root and subRoot:
            return self.isSubtree(root.left , subRoot) or self.isSubtree(root.right ,subRoot) or self.dfsHelper(root,subRoot)
        else:
            return False

        



    def dfsHelper(self,root: Optional[TreeNode],subRoot:Optional[TreeNode]) -> bool:
        if root == subRoot == None:
            return True
        if root and subRoot and root.val == subRoot.val:
            return self.dfsHelper(root.left, subRoot.left) and self.dfsHelper(root.right, subRoot.right)
        else:
            return False