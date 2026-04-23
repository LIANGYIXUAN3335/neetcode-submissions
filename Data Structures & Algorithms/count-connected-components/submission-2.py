class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # solution 1 dfs
        nodeMap = {i : [] for i in range(n)}
        for node1,node2 in edges:
            nodeMap[node1].append(node2)
            nodeMap[node2].append(node1)
        visited = set()
        # def dfs(node):
        #     if node in visited:
        #         return
        #     visited.add(node)
        #     for i in nodeMap[node]:
        #         dfs(i)             
        # res = 0
        # for i in range(n):
        #     if i not in visited:
        #         dfs(i)
        #         res += 1
        # return res
        # solution 2 bfs
        def bfs(node):
            q = deque()
            q.append(node)
            while q:
                node = q.popleft()
                visited.add(node)
                for i in nodeMap[node]:
                    if i in visited:
                        continue
                    q.append(i)
        res = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                res += 1
        return res
             
        # solution 3 disjoint set union
    # solution 3 DSU
#         dsu = DSU(n)
#         for edge in edges:
#             if dsu.union(edge[0],edge[1]):
#                 dsu.comp -= 1
#         return dsu.comp 

# class DSU:
#     def __init__(self,n):
#         self.comp = n
#         self.Parents = [i for i in range(n + 1)]
#         self.Size = [1 for _ in range(n + 1)]
#     def find(self,node):
#         if self.Parents[node] != node:
#             self.Parents[node] = self.find(self.Parents[node])
#         return self.Parents[node]
#     def union(self,node1,node2):
#         p1 , p2 = self.find(node1), self.find(node2)
#         if p1 == p2 :
#             return False
#         if self.Size[p1] >= self.Size[p2]:
#             self.Parents[p2] = p1
#             self.Size[p2] = self.Size[p1]
#         else:
#             self.Parents[p1] = p2
#             self.Size[p1] = self.Size[p2]
#         return True

