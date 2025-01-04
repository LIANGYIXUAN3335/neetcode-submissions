# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #solution 1 recursion
        # def dp(head:Optional[ListNode]) -> Optional[ListNode]:
        #     if not head or not head.next:
        #         return head
        #     newHead = dp(head.next)
        #     head.next.next = head
        #     head.next = None
        #     return newHead
        # return dp(head)
        #solution 2 iteration
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

        