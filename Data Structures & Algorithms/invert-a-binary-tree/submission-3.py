from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        rootQueue = deque([root])
        while rootQueue:
            curRoot = rootQueue.popleft()
            if not curRoot:
                continue
            # 交换左右子节点
            curRoot.left, curRoot.right = curRoot.right, curRoot.left
            # 这里要用 curRoot 而不是 root
            if curRoot.left:
                rootQueue.append(curRoot.left)
            if curRoot.right:
                rootQueue.append(curRoot.right)
        return root