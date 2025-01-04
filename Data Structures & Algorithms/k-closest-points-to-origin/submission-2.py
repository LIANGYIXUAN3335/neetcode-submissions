from math import sqrt, pow
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        newList = []
        for i in points:
            distance = -1 * sqrt(pow(i[0], 2) + pow(i[1], 2))
            heapq.heappush(newList,([distance,tuple(i)]))
            if len(newList) > k:
                heapq.heappop(newList)
        for i in range(k):
            res.append(list(heapq.heappop(newList)[1]))
        return res        