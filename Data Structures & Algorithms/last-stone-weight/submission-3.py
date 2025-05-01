class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [- stone for stone in stones]
        heapq.heapify(minHeap)
        while len(minHeap) > 1:
            left = heapq.heappop(minHeap)
            right= heapq.heappop(minHeap)
            leftover= left - right
            if left < 0:
                heapq.heappush(minHeap, leftover)
        if len(minHeap) > 0:
            return -minHeap[0]
        return 0
        