# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {}
        for i in range(len(inorder)):
            inorderMap[inorder[i]] = i
        def helper(preStart : int, preEnd : int, inStart : int, inEnd : int) -> Optional[TreeNode]:
            if preStart > preEnd:
                return None
            root = TreeNode(preorder[preStart])
            inOrderIndex = inorderMap[preorder[preStart]]
            leftLen = inOrderIndex - inStart
            rightLen = inEnd - inOrderIndex
            root.left = helper(preStart + 1, preStart + leftLen, inStart, inOrderIndex - 1 )
            root.right = helper(preStart + leftLen + 1, preEnd, inOrderIndex + 1, inEnd)
            return root
        return helper(0, len(preorder) - 1, 0, len(preorder) - 1)
        