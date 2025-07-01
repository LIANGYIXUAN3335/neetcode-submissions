class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        m = len(grid)
        n = len(grid[0])
        def dfs(i : int, j : int, curDistance : int) -> None:
            if curDistance != 0 and grid[i][j] <= curDistance:
                return
            grid[i][j] = curDistance
            for x , y in directions:
                curI, curJ = x + i, y + j
                if curI < 0 or curJ < 0 or  curI >= m or curJ >= n or grid[curI][curJ] == -1 or grid[curI][curJ] == 0 :
                    continue
                dfs(curI, curJ , curDistance + 1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j, 0)
        