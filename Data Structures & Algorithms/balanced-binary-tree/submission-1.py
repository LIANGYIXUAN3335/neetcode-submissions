# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # solution1 brute force -- have a function to calculate the height for each node and compare them
        # which is not recommended, cause we can update the res in the recursion and will use On time complexity
        # solution 2 recursion dfs time Com--  On and space comp -- O logn to O(n)
        # self.res = True
        # def dfs(root: Optional[TreeNode]) -> int:
        #     if not root:
        #         return 0
        #     leftDep = dfs(root.left)
        #     rightDep = dfs(root.right)
        #     if abs(leftDep - rightDep) > 1:
        #         self.res = False
        #     return max(leftDep,rightDep) + 1
        # dfs(root)
        # return self.res
        # solution 3 iterative dfs -- the trick is that in the map when the node is None 
        # every Node which is None is the same
        nodeHeightMap = {None :  0}
        if not root:
            return True
        stack = [root]
        while stack:
            curRoot = stack[-1]
            if not curRoot:
                continue
            if curRoot.left and curRoot.left not in nodeHeightMap: 
                stack.append(curRoot.left)
            elif curRoot.right and curRoot.right not in nodeHeightMap:
                stack.append(curRoot.right)
            else:
                curNode = stack.pop()
                leftHeight = nodeHeightMap[curNode.left]
                rightHeight = nodeHeightMap[curNode.right]
                if abs(leftHeight - rightHeight) > 1:
                    return False
                nodeHeightMap[curNode] = max(leftHeight,rightHeight) + 1
        return True
            