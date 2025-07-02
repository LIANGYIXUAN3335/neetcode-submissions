class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        leftGoodFruit = 0
        m = len(grid)
        n = len(grid[0])
        q = deque()  
        time = -1
        directions =[[1,0] ,[0,1], [-1,0],[0 , -1]]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    leftGoodFruit += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        if leftGoodFruit ==0 :
            return 0
        while len(q) > 0:
            time += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for x, y in directions:
                    curI, curJ = i + x , j + y
                    if curI < 0 or curJ < 0 or curI >= m or curJ >= n or grid[curI][curJ] == 0 or grid[curI][curJ] == 2:
                        continue
                    grid[curI][curJ] = 2
                    leftGoodFruit -= 1
                    q.append((curI, curJ))  
        return time if leftGoodFruit == 0 else -1