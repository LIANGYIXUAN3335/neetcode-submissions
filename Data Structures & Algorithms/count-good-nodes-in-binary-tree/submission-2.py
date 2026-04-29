# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root: TreeNode, curMax : int) :
            if not root:
                return
            if curMax <= root.val:
                self.res += 1
            dfs(root.left, max(curMax , root.val))
            dfs(root.right, max(curMax, root.val))
        dfs(root,-101)
        return self.res

        