class Solution:
    def isHappy(self, n: int) -> bool:
        # solution 1 hashset
        # numSet = set()
        # def getHappyNum(n):
        #     return sum([int(i) ** 2 for i in str(n)])
        # cur = getHappyNum(n)        
        # while cur != 1:
        #     if cur in numSet:
        #         return False
        #     numSet.add(cur)
        #     cur = getHappyNum(cur)
        # return True
        # solution 2 fast and slow pointer
        def getHappyNum(n):
            return sum([int(i) ** 2 for i in str(n)])
        fast = getHappyNum(getHappyNum(n))
        slow = getHappyNum(n)
        while fast != slow:
            fast = getHappyNum(getHappyNum(fast))
            slow = getHappyNum(slow)
        if fast == 1:
            return True
        else:
            return False
        