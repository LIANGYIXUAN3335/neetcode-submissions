# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        preNode = None
        curNode = head
        while curNode.next:
            tempNext = curNode.next
            curNode.next = preNode
            preNode = curNode
            curNode = tempNext
        curNode.next = preNode
        return curNode

        