# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #solution1 dfs helper funciton with self reslist 
        self.res = []
        def dfs(root:Optional[TreeNode],index) ->None:
            if not root:
                return
            if len(self.res) == index:
                self.res.append([root.val])
            else:
                self.res[index].append(root.val)
            dfs(root.left,index + 1)
            dfs(root.right,index + 1)
        dfs(root,0)
        return self.res
                

        