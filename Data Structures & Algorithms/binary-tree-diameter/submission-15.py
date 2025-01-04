# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #solution1 recursion dfs
        # self.res = 0
        # def getMaxDepth(root :Optional[TreeNode]):
        #     if not root:
        #         return 0
        #     leftDep =getMaxDepth(root.left)
        #     rightDep = getMaxDepth(root.right)
        #     self.res= max(self.res, leftDep+ rightDep)
        #     return max(getMaxDepth(root.left), getMaxDepth(root.right)) + 1
        # getMaxDepth(root)
        # return self.res
        #solution 2 brute force
    #     if not root:
    #         return 0
    #     rootLength = self.getMaxDepth(root.left) + self.getMaxDepth(root.right)
    #     subMaxLength = max(self.diameterOfBinaryTree(root.left) ,self.diameterOfBinaryTree(root.right))
    #     return max(subMaxLength, rootLength)


    # def getMaxDepth(self , root :Optional[TreeNode]):
    #     if not root:
    #         return 0
    #     leftDep =self.getMaxDepth(root.left)
    #     rightDep = self.getMaxDepth(root.right)
    #     return max(leftDep, rightDep) + 1
        #solution3 iterative dfs
        res = 0
        nodeMap = {}
        if not root:
            return 0
        def getMaxDepth( root :Optional[TreeNode]):
            if not root:
                nodeMap[root]  = 0
                return 0  
            leftDep =getMaxDepth(root.left)
            rightDep = getMaxDepth(root.right)
            nodeMap[root] = max(leftDep, rightDep) + 1
            return max(leftDep, rightDep) + 1
        getMaxDepth(root)
        nodeStack = [root]
        res = 0
        while nodeStack :
            curRoot = nodeStack.pop()
            if not curRoot:
                continue
            res = max(nodeMap[curRoot.left] + nodeMap[curRoot.right] ,res)
            nodeStack.append(curRoot.left)
            nodeStack.append(curRoot.right)
        return res
        

        