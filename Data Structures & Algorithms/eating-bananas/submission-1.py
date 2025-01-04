class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        maxPerHour = max(piles)
        minPerHour = 1
        # we want to get the uper bound in the question 
        while minPerHour < maxPerHour:
            mid = (maxPerHour - minPerHour) // 2 + minPerHour
            curHours = 0
            for i in piles:
                curHours += math.ceil(i/mid)
            if curHours > h:
                minPerHour = mid + 1
            else:
                maxPerHour = mid
        return int(minPerHour)

        