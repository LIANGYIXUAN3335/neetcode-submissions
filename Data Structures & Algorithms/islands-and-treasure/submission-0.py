from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #solution 1 multi source bfs
        Inf = 2147483647
        m, n= len(grid),len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        while  q:
            curPos =  q.popleft()
            for d in directions:
                i , j = curPos[0] + d[0] ,curPos[1] +d[1]
                if i >= m or j >= n or i <0 or j < 0 or grid[i][j] != Inf:
                    continue
                grid[i][j] = grid[curPos[0]][curPos[1]] + 1
                q.append((i,j))

            

        #solution 2 bfs
