class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for edge in edges:
            if dsu.union(edge[0],edge[1]):
                dsu.comp -= 1
        return dsu.comp 

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
