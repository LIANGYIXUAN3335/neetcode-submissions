# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curRoot = root
        while curRoot:
            if curRoot.val > q.val and curRoot.val > p.val :
                curRoot = curRoot.left
            elif curRoot.val < q.val and curRoot.val < p.val:
                curRoot = curRoot.right
            else:
                return curRoot
        return curRoot

        