# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow, fast = head, head
        while fast and fast.next:
            slow= slow.next
            fast = fast.next.next
        fast = slow.next
        slow.next= None
        pre, cur= None, fast
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        start = ListNode(-1)
        flag = False
        while pre and head:
            if not flag:
                start.next = head
                head = head.next
            else:
                start.next = pre
                pre = pre.next
            start = start.next
            flag = not flag 
        if head:
            start.next= head
