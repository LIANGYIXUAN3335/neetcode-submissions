class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        if n == 1:
            return True
        cur = n
        while cur not in seen:
            seen.add(cur)
            if cur == 1:
                return True
            newCur = 0
            for i in str(cur):
                newCur += int(i) * int(i)
            cur = newCur
        return False
        
            