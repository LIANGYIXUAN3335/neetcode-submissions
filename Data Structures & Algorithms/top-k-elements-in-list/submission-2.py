class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

    # 1st solution: sorting
    # first solution -- use sorted( time complexity is Nlogn and space complexity is N)
    # why the space complexity is O(n) rather than O(k)
    # cause in worst case the hash table's length will be n
    # create a hash table 
        # numCount = {}
        # for i in nums:
        #     numCount[i] = numCount.get(i,0) + 1
        # arr = []
        # for num, cnt in numCount.items():
        #     arr.append([cnt,num])
        # arr.sort()
        # res = []
        # while len(res) < k:
        #     res.append(arr.pop()[1])
        # return res
    # 2nd solution:
    # use maxHeap
    # cause we want to have only top k elements, so if we use 
    # maxheap.pop will use logn and we pop k times so the time 
    # complexity will be klogn and the maxheap will have length n ,
    # wo the space complexity will be N
        numCount ={}
        for i in nums:
            numCount[i] = numCount.get(i,0) +1 
        maxHeap = []
        for num, count in numCount.items():
            heapq.heappush(maxHeap,[-count,num])
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        return res


    