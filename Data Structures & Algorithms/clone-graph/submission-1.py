"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # solution 1 dfs
        # nodeMap = {None:None}
        # def dfs(node):
        #     if node in nodeMap.keys():
        #         return nodeMap[node]
        #     curNode = Node(node.val)
        #     nodeMap[node] = curNode
        #     neighborsList = []
        #     for i in node.neighbors:
        #         neighborsList.append(dfs(i))
        #     curNode.neighbors = neighborsList
        #     return curNode
        # dfs(node)
        # return nodeMap[node]
        # solution 2 bfs
        if not node:
            return None
        nodeMap = {node:Node(node.val)}
        q = deque()
        q.append(node)
        while q:
            cur = q.popleft()
            copyNeighbors = []
            for neighbor in cur.neighbors:
                if neighbor not in nodeMap.keys():
                    nodeMap[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                nodeMap[cur].neighbors.append(nodeMap[neighbor])
        return nodeMap[node]


