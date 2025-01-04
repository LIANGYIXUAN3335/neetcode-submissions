from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # solution 1 : multi start bfs
        q = deque()
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visited[i][j] =True
                elif grid[i][j] == 1:
                    fresh += 1
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        minute = 0
        while q:
            costMinute = 0
            for _ in range(len(q)):
                cur = q.popleft()
                for di,dj in directions:
                    curI,curJ = cur[0] + di, cur[1] + dj
                    if curI <0 or curJ < 0 or curI >= m or curJ >= n or visited[curI][curJ] == True:
                        continue
                    visited[curI][curJ] = True
                    if grid[curI][curJ] == 1:
                        costMinute = 1
                        q.append((curI,curJ))
                        grid[curI][curJ] = 2
                        fresh -= 1
                        
            minute += costMinute
        
        return minute if fresh ==0 else -1
        





        