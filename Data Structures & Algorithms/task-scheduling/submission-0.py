from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0
        while q or maxHeap:
            time += 1
            if maxHeap:
                curTaskCount = heapq.heappop(maxHeap) + 1
                if curTaskCount:
                    q.append([curTaskCount,time + n])
            else:
                time = q[0][1]
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
            





        
