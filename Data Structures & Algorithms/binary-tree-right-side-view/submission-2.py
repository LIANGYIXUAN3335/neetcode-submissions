# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # solution1 recursive dfs
        # self.res = []
        # def dfsHelper(root: Optional[TreeNode],index):
        #     if not root:
        #         return
        #     if index >= len(self.res):
        #         self.res.append(root.val)
        #     else:
        #         self.res[index] = root.val
        #     dfsHelper(root.left,index + 1)
        #     dfsHelper(root.right,index +1)
        # dfsHelper(root,0)
        # return self.res
        #solution 2 bfs with queue
        queue = deque()
        queue.append(root)
        index = 0
        res = []
        while queue:
            for i in range(len(queue)):
                curNode = queue.popleft()
                if not curNode:
                    continue
                if len(res) == index:
                    res.append(curNode.val)
                if curNode.right:
                    queue.append(curNode.right)
                if curNode.left:
                    queue.append(curNode.left)
            index += 1
        return res

                



        