class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [100001] * n
        dist[src] = 0
        curStop = 0

        for i in range(k + 1):
            memo = dist.copy()
            for start, end, weight in flights:
                if memo[start] + weight < dist[end]:
                    dist[end] = memo[start] + weight
            
        return dist[dst] if dist[dst] != 100001 else -1


        