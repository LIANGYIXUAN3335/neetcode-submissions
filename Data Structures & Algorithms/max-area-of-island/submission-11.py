class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        self.curMax = 0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        def dfs(i, j) -> None:
            grid[i][j] = 0
            self.curMax += 1
            for x , y in directions:
                curI, curJ = i +x , j + y
                if curI < 0 or curJ < 0 or curI >= len(grid) or curJ >= len(grid[0]):
                    continue
                if grid[curI][curJ] == 1:
                    dfs(curI, curJ)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.curMax = 0
                    dfs(i, j)
                    res = max(res, self.curMax)
        return res