class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = [False] * n
        self.res = True
        def dfs(node,parent):
            visited[node] = True
            if not self.res:
                return
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if  visited[neighbor]:
                    self.res = False
                else:
                    dfs(neighbor, node)
        dfs(0, None)
        if False in visited:
            return False
        return self.res 


        