from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # solution 2 dfs
        directions = [(-1,0),(0,-1),(0,1),(1,0)]
        m = len(heights)
        n = len(heights[0])
        pacVisit, atlVisit = [[False] * n for _ in range(m)] ,[[False] * n for _ in range(m)] 
        def dfs(cur,visited):
            for di,dj in directions:
                curI, curJ = cur[0] + di , cur[1] + dj
                if curI <0 or curJ <0 or curI >= m or curJ >=n or visited[curI][curJ] == True:
                    continue
                if heights[curI][curJ] >= heights[cur[0]][cur[1]]:
                    visited[curI][curJ] = True
                    dfs((curI,curJ),visited)
        for i in range(n):
            pacVisit[0][i] =True
            dfs((0,i),pacVisit)
            atlVisit[m-1][i] = True
            dfs((m - 1, i),atlVisit)
        for j in range(m):
            pacVisit[j][0] = True
            dfs((j,0),pacVisit)
            atlVisit[j][n-1] = True
            dfs((j,n-1),atlVisit)
        res = []
        for i in range(m):
            for j in range(n):
                if pacVisit[i][j] and atlVisit[i][j]:
                    res.append([i,j])
        return res
            

                        




        