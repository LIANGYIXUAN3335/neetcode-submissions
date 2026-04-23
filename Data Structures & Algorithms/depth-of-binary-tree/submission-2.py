# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # solution 1 recrusion dfs
        # if not root:
        #     return 0
        # return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1; 
        # solution 2: bfs
        # if not root:
        #     return 0
        # queue = deque([root])
        # level = 0
        # while queue:
        #     level  += 1
        #     for i in range(len(queue)):
        #         curRoot = queue.popleft()
        #         if curRoot.left:
        #             queue.append(curRoot.left)
        #         if curRoot.right:
        #             queue.append(curRoot.right)
        # return level
        # solution 3 iterative dfs
        stack = []
        stack.append((root,0))
        maxDep = 0
        while stack:
            curNode = stack.pop()                
            if not curNode[0]:
                maxDep = max(maxDep,curNode[1]) 
                continue
            stack.append((curNode[0].left,curNode[1] + 1))
            stack.append((curNode[0].right,curNode[1] + 1))
        return maxDep



            
        