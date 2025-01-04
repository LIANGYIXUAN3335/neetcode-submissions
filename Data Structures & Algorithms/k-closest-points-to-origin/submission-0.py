from math import sqrt, pow
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        newList = []
        for i in points:
            distance = sqrt(pow(i[0], 2) + pow(i[1], 2))
            newList.append([distance,tuple(i)])
        heapq.heapify(newList)
        res = []
        for i in range(k):
            res.append(list(heapq.heappop(newList)[1]))
        return res        