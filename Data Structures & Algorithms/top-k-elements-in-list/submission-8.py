class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDic = {}
        res = []
        for i in nums:
            numsDic[i] = numsDic.get(i,0) +1
        maxHeap = []
        for key,value in numsDic.items():
            heapq.heappush(maxHeap,[value,key])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        for i in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        return res