class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        def getTime(speed : int) -> int:
            res = 0
            for i in piles:
                res += i // speed
                if i % speed > 0:
                    res += 1
            return res
        res = right
        while left< right:
            mid = left +(right - left ) // 2
            curCost = getTime(mid)
            if curCost > h:
                left = mid + 1
            else:
                res = min(res, mid)
                right = mid 
        return res