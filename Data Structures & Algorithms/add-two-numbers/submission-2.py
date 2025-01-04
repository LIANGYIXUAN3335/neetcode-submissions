# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0,None)
        cur = res
        addOn = 0
        while l1 or l2:
            curSum = 0
            if l1:
                curSum += l1.val
                l1 = l1.next
            if l2:
                curSum += l2.val
                l2 = l2.next
            curVal = (curSum + addOn) % 10
            cur.next = ListNode(curVal,None)
            addOn = (curSum + addOn) // 10
            cur = cur.next
        if addOn != 0:
            cur.next = ListNode(addOn,None)
        return res.next
            
        
        