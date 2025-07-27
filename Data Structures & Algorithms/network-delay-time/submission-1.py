class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for fro, to, dis in times:
            graph[fro].append((dis, to))
        hq = []
        visited = set()
        heapq.heappush(hq, (0 ,k))
        res = 0
        while hq:
            dis, curNode = heapq.heappop(hq)
            if curNode in visited:
                continue
            res = dis
            visited.add(curNode)
            for curDis, to in graph[curNode]:
                if to in visited:
                    continue
                heapq.heappush(hq, (dis + curDis, to))
        
        return res if len(visited) == n else -1