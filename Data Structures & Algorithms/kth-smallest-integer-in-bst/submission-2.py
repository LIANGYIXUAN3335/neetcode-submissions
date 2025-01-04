# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # solution 1 recursive dfs with res in a list
        # res = []
        # def dfsHelper(root : Optional[TreeNode]) -> None:
        #     if not root:
        #         return
        #     dfsHelper(root.left)
        #     res.append(root.val)
        #     dfsHelper(root.right)
        # dfsHelper(root)
        # return res[k - 1]
        # solution 2 recursive dfs with res return early
        # self.k = k
        # self.res = root.val
        # def dfsHelper(root : Optional[TreeNode]) -> None:
        #     if root:
        #         dfsHelper(root.left)
        #         if self.k == 1:
        #             self.res = root.val
        #         self.k -= 1
        #         dfsHelper(root.right)
        # dfsHelper(root)
        # return self.res
        # solution 3
        stack = []
        stack.append(root)
        visited = []
        while stack:
            curRoot =  stack[-1]
            while curRoot.left and curRoot.left not in visited:
                stack.append(curRoot.left)
                curRoot = curRoot.left
            curNode = stack.pop()
            visited.append(curNode)
            k -= 1
            if k == 0:
                return curNode.val
            if curNode.right:
                stack.append(curNode.right)




