class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # solution 1 dfs
        if len(edges) != n-1:
            return False
        # nodeMap = {i : [] for i in range(n)}
        # for node1,node2 in edges:
        #     nodeMap[node1].append(node2)
        #     nodeMap[node2].append(node1)
        # visited = set()
        # def dfs(node, parent):
        #     if node in visited:
        #         return False
        #     visited.add(node)
        #     for i in nodeMap[node]:
        #         if i == parent:
        #             continue
        #         if dfs(i,node) == False:
        #             return False
        #     visited.remove(node)
        #     return True
        # return dfs(0,-1)
        # solution 2 bfs
        # q = deque()
        # q.append((0,-1))
        # while q:
        #     cur =  q.popleft()
        #     node,parent = cur[0], cur[1]
        #     if node in visited:
        #         return False
        #     visited.add(node)
        #     for i in nodeMap[node]:
        #         if i == parent:
        #             continue
        #         q.append((i,node))
        # if len(visited) == n:
        #     return True
        # return False        
        # solution 3 disjoint set union
        dsu = DSU(n)
        for edge in edges:
            if dsu.union(edge[0],edge[1]) == False:
                return False
            dsu.comp -= 1
        return dsu.comp == 1

class DSU:
    def __init__(self,n):
        self.comp = n
        self.Parents = [i for i in range(n + 1)]
        self.Size = [1 for _ in range(n + 1)]
    def find(self,node):
        if self.Parents[node] != node:
            self.Parents[node] = self.find(self.Parents[node])
        return self.Parents[node]
    def union(self,node1,node2):
        p1 , p2 = self.find(node1), self.find(node2)
        if p1 == p2 :
            return False
        if self.Size[p1] >= self.Size[p2]:
            self.Parents[p2] = p1
            self.Size[p2] = self.Size[p1]
        else:
            self.Parents[p1] = p2
            self.Size[p1] = self.Size[p2]
        return True



        