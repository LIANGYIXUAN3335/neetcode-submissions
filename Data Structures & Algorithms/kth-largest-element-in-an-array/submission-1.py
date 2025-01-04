import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for i in nums:
            heapq.heappush(res,i)
            if len(res) > k:
                heapq.heappop(res)
        return heapq.heappop(res)
        