# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def helper(start, end) -> Optional[ListNode]:
            if start == end:
                return lists[start]
            mid = start + (end - start) // 2
            left = helper(start, mid)
            right = helper(mid + 1, end)
            dummy = ListNode(-1)
            cur = dummy
            while left and right:
                if left.val > right.val:
                    cur.next = right
                    cur = cur.next
                    right = right.next
                else:
                    cur.next = left
                    cur = cur.next
                    left = left.next
            if left:
                cur.next = left
            else:
                cur.next= right
            return dummy.next
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        return helper(0, len(lists) - 1)
        

        