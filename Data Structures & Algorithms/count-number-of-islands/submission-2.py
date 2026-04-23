class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i ,j ):
            grid[i][j] ="0"
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            for direction in directions:
                cur = [i + direction[0], j + direction[1]]
                if cur[0] < m and cur[0] >= 0 and cur[1] < n and cur[1] >= 0:
                    if grid[cur[0]][cur[1]] == "1":
                        dfs(cur[0],cur[1])
                    
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    res += 1
        return res
