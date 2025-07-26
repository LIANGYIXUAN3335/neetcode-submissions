class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        unionSet = UnionSet(len(edges))
        for fro, to in edges:
            if unionSet.isConnected(fro - 1, to - 1):
                return [fro, to]
            
            unionSet.union(fro - 1, to - 1)
        return []

class UnionSet:
    def __init__(self , n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    def isConnected(self, node1, node2):
        return self.find(node1)  == self.find(node2)

    def union(self, node1, node2):
        if self.find(node1) == self.find(node2):
            return 
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        if self.size[parent1] > self.size[parent2]:
            self.parent[parent2] = parent1
            self.size[parent1] += self.size[parent2]
        else:
            self.parent[parent1] = parent2
            self.size[parent2] = parent1

    def find(self,node):
        if self.parent[node] != self.parent[self.parent[node]]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]