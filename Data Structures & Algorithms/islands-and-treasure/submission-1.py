from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #solution 1 multi source bfs
        # Inf = 2147483647
        # m, n= len(grid),len(grid[0])
        # q = deque()
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 0:
        #             q.append((i,j))
        # directions = [(-1,0),(0,1),(1,0),(0,-1)]
        # while  q:
        #     curPos =  q.popleft()
        #     for d in directions:
        #         i , j = curPos[0] + d[0] ,curPos[1] +d[1]
        #         if i >= m or j >= n or i <0 or j < 0 or grid[i][j] != Inf:
        #             continue
        #         grid[i][j] = grid[curPos[0]][curPos[1]] + 1
        #         q.append((i,j))
        #solution 2 bfs
        m, n= len(grid),len(grid[0])
        Inf = 2147483647
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        def bfs(i,j):
            visited = set()
            dis = 1
            q = deque()
            q.append((i,j))
            while q:
                for i in range(len(q)):
                    i ,j = q.popleft()
                    visited.add((i,j))
                    for di,dj in directions:
                        curi , curj = i + di ,j + dj
                        if curi >= m or curj >= n or curi <0 or curj < 0 or grid[curi][curj] == -1 or (curi,curj) in visited:
                            continue
                        if grid[curi][curj] == 0:
                            return dis
                        q.append((curi,curj))
                dis += 1
            return Inf
        for i in range(m):
            for j in range(n):
                if grid[i][j] == Inf:
                    grid[i][j] = bfs(i,j)
                
                



