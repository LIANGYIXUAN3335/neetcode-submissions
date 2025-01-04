class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1st solution 
        # creat dict key - num value count
        # array.sort([count,num]) 
        # res = [] --k 
        # time complexity -- nlogn space complexity n
        # numCount = {}
        # for i in nums:
        #     numCount[i] = numCount.get(i,0) + 1
        # numSort = []
        # for num,count in numCount.items():
        #     numSort.append([count,num])
        # numSort.sort()
        # res = []
        # for i in range(len(numSort)-1,-1,-1):
        #     res.append(numSort[i][1])
        #     if len(res) ==k :
        #         return res
        # 2nd solution maxHeap 
        # creat dict
        # array[-count,num]
        # heapq.pop[1] time complexity : klogn space complexity o (n)
        numCount = {}
        for i in nums:
            numCount[i] = numCount.get(i,0) + 1
        maxHeap = []
        for num, count in numCount.items():
            heapq.heappush(maxHeap, [-count,num])
        res = []
        for i in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        return res





        
        


    