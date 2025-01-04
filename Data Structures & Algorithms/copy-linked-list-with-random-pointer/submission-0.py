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
        nodeMap = {None :None}
        cur = head
        while cur:
            copyCur = Node(cur.val,None,None)
            nodeMap[cur] = copyCur
            cur = cur.next
        cur = head
        while cur:
            copyCur = nodeMap[cur]
            copyCur.next = nodeMap[cur.next]
            copyCur.random = nodeMap[cur.random]
            cur = cur.next
        return nodeMap[head]
        
        