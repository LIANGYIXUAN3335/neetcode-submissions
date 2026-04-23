# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # solution 1 bfs
        rootQueue = deque([root])
        while rootQueue:
            curRoot = rootQueue.popleft()
            if not curRoot:
                continue
            curRoot.left,curRoot.right = curRoot.right,curRoot.left
            if curRoot.left:
                rootQueue.append(curRoot.left)
            if curRoot.right:
                rootQueue.append(curRoot.right)
        return root
