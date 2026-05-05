class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dis = abs(x1-x2) + abs(y1 - y2)
                edges.append((dis, i, j))
        heapq.heapify(edges)
        unionSet = UnionSet(n)
        usedEdges = 0
        res = 0
        while usedEdges < n - 1:
            dis, i , j = heapq.heappop(edges)
            if unionSet.isConnected(i, j):
                continue
            res += dis
            unionSet.union(i, j)
            usedEdges += 1
        return res

        
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
            self.size[parent2] += parent1

    def find(self,node):
        if self.parent[node] != self.parent[self.parent[node]]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]