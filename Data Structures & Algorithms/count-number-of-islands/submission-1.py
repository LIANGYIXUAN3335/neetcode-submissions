class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited =[[False for j in range(n)] for i in range(m)]

        def dfs(i ,j ):
            visited[i][j] = True
            if grid[i][j] == "0":
                return
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            for direction in directions:
                cur = [i + direction[0], j + direction[1]]
                if cur[0] < m and cur[0] >= 0 and cur[1] < n and cur[1] >= 0:
                    if not visited[cur[0]][cur[1]]:
                        dfs(cur[0],cur[1])
                    
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and visited[i][j] == False:
                    dfs(i,j)
                    res += 1
        return res
