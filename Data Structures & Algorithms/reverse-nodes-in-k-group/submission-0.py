# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 1
        cur = head
        while count < k and cur:
            cur= cur.next
            count += 1
        if count < k or not cur:
            return head
        nextNode = self.reverseKGroup(cur.next, k)
        cur.next = None
        cur = head
        pre = None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        head.next = nextNode
        return pre
        

        
    