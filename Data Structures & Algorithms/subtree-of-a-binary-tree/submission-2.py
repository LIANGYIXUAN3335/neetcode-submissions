# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res = False
        self.helper(root,subRoot)
        return self.res
    def helper(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.res or not root: 
            return
        if root and root.val == subRoot.val:
            if self.isSameTree(root,subRoot):
                self.res = True
        self.helper(root.left, subRoot) 
        self.helper(root.right, subRoot)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        