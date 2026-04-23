import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minList = [ -1 * i for i in stones]
        heapq.heapify(minList)
        while len(minList) > 1:
            stone1 = heapq.heappop(minList)
            stone2 = heapq.heappop(minList)
            if stone2 > stone1:
                heapq.heappush(minList,(stone1-stone2))
        if len(minList) == 1:
            return -1 * minList[0]
        else:
            return 0
        