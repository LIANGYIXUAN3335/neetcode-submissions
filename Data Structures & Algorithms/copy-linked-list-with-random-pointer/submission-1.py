"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeMap = {None: None}
        curNode = head
        while curNode:
            curCopy = Node(curNode.val)
            nodeMap[curNode] = curCopy
            curNode= curNode.next
        curNode = head
        while curNode:
            curCopy = nodeMap[curNode]
            curCopy.next= nodeMap[curNode.next]
            curCopy.random = nodeMap[curNode.random]
            curNode = curNode.next
        return nodeMap[head]
        