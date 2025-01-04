# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #solution1 dfs helper funciton with self reslist 
        # self.res = []
        # def dfs(root:Optional[TreeNode],index) ->None:
        #     if not root:
        #         return
        #     if len(self.res) == index:
        #         self.res.append([root.val])
        #     else:
        #         self.res[index].append(root.val)
        #     dfs(root.left,index + 1)
        #     dfs(root.right,index + 1)
        # dfs(root,0)
        # return self.res
        # solution 2 -  bfs with queu
        queue = deque()
        queue.append(root)
        index = 0
        res = []
        if not root:
            return []
        while queue:
            curList = []
            for i in range(len(queue)):
                curNode = queue.popleft()
                curList.append(curNode.val)
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
            res.append(curList)
            index += 1
        return res

                

        