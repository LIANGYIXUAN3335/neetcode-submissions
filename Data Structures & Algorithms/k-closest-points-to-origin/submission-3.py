class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for  x, y in points:
            distance = (x * x + y * y )
            heapq.heappush(minHeap, [-distance, x, y])
            while len(minHeap) > k:
                heapq.heappop(minHeap)
        return [[x,y] for _, x, y in minHeap]

        