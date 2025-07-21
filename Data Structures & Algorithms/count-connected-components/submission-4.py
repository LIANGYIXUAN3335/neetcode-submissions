class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = [False] * n
        self.res = 0
        def dfs(node):
            visited[node] = True
            if not self.res:
                return
            for neighbor in graph[node]:
                if  visited[neighbor]:
                    continue
                else:
                    dfs(neighbor)
        for node in range(n):
            if visited[node]:
                continue
            else:
                self.res += 1
                dfs(node)
        return self.res 
