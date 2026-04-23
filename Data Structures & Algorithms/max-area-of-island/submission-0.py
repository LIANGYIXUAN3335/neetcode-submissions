class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # solution 1
        rowLen, colLen = len(grid),len(grid[0])
        maxArea = 0
        directions = [(1,0),(0,1),(0,-1),(-1,0)]
        def dfs(i,j):
            grid[i][j] = 0
            area = 1
            for di,dj in directions:
                curI,curJ = di + i, dj + j 
                if curI >= rowLen or curJ >= colLen or curI <0 or curJ <0 or grid[curI][curJ] == 0:
                    continue
                area += dfs(curI,curJ)
            return area
        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == 1:
                    maxArea = max(maxArea,dfs(i,j))
        return maxArea

                

            



        