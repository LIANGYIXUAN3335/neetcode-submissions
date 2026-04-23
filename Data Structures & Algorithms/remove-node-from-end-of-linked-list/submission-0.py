# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # solution 1 - two pass
        length = 0
        cur = head
        dummy = ListNode(0,head)
        while cur != None:
            length += 1
            cur = cur.next
        index = length - n
        cur = dummy
        curIndex = 0
        while cur:
            if curIndex == index:
                cur.next = cur.next.next
                break
            cur = cur.next
            curIndex += 1
        return dummy.next

        # solution 2 - recursion

        # solution 3 - two pointer
        