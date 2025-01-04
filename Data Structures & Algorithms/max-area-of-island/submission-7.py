from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rowLen, colLen = len(grid),len(grid[0])
        dsu = DSU(rowLen * colLen)
        directions = [(1,0),(0,1),(0,-1),(-1,0)]
        area = 0
        def index(r, c):
            return r * colLen + c

        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == 1:
                    for dr, dc in directions:
                        curR,curC = i + dr, j + dc
                        if (curR < 0 or curC < 0 or curR >= rowLen or curC >= colLen or grid[curR][curC] == 0):
                            continue
                        dsu.union(index(i, j), index(curR, curC))
                    area = max(area, dsu.getSize(index(i, j)))

        return area
        # solution 1
        # rowLen, colLen = len(grid),len(grid[0])
        # maxArea = 0
        # directions = [(1,0),(0,1),(0,-1),(-1,0)]
        # def dfs(i,j):
        #     grid[i][j] = 0
        #     area = 1
        #     for di,dj in directions:
        #         curI,curJ = di + i, dj + j 
        #         if curI >= rowLen or curJ >= colLen or curI <0 or curJ <0 or grid[curI][curJ] == 0:
        #             continue
        #         area += dfs(curI,curJ)
        #     return area
        # for i in range(rowLen):
        #     for j in range(colLen):
        #         if grid[i][j] == 1:
        #             maxArea = max(maxArea,dfs(i,j))
        # return maxArea
        # solution 2
        # rowLen, colLen = len(grid),len(grid[0])
        # maxArea = 0
        # directions = [(1,0),(0,1),(0,-1),(-1,0)]
        # def bfs(i,j):
        #     queue = deque()
        #     queue.append([i,j])
        #     area = 1
        #     grid[i][j] = 0
        #     while queue:
        #         curPos = queue.popleft()
        #         for di, dj in directions:
        #             curi,curj = curPos[0] + di, curPos[1] + dj
        #             if curi < 0 or curj < 0 or curi >= rowLen or curj >= colLen or grid[curi][curj] == 0:
        #                 continue
        #             grid[curi][curj] = 0
        #             area += 1
        #             queue.append([curi,curj])
        #     return area      
        # for i in range(rowLen):
        #     for j in range(colLen):
        #         if grid[i][j] == 1:
        #             maxArea = max(maxArea,bfs(i,j))
        # return maxArea
        # solution 3 disjoint set union
class DSU:
    def __init__(self,n):
        self.Parents = [i for i in range(n+1)]
        self.Size = [1 for i in range(n+1)]
        self.Max = 0
    
    def find(self,node):
        if self.Parents[node] != node:
            self.Parents[node] = self.find(self.Parents[node])
        return self.Parents[node]
    def getSize(self, node):
        par = self.find(node)
        return self.Size[par]

    def union(self,node1,node2):
        pNode1 = self.find(node1)
        pNode2 = self.find(node2)
        if pNode1 != pNode2:
            if self.Size[pNode1] > self.Size[pNode2]:
                self.Size[pNode1] += self.Size[pNode2]
                self.Parents[pNode2] = pNode1
                self.Max = max(self.Max, self.Size[pNode1])
            else:
                self.Size[pNode2] += self.Size[pNode1]
                self.Parents[pNode1] = pNode2
                self.Max = max(self.Max, self.Size[pNode2])
            

                

            



        