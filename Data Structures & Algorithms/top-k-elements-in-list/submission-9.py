import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDic = {}
        minHeap = []
        for i in nums:
            numsDic[i] = numsDic.get(i,0) + 1
        for key,value in numsDic.items():
            heapq.heappush(minHeap,[value,key])
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        res = [i[1] for i in minHeap]
        return res