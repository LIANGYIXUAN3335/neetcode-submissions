from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # solution 1 bfs
        directions = [(-1,0),(0,-1),(0,1),(1,0)]
        m = len(heights)
        n = len(heights[0])
        pacVisit, atlVisit = [[False] * n for _ in range(m)] ,[[False] * n for _ in range(m)] 
        def bfs(queue,visited):
            while queue:
                cur = queue.popleft()
                for di,dj in directions:
                    curI, curJ = cur[0] + di , cur[1] + dj
                    if curI <0 or curJ <0 or curI >= m or curJ >=n or visited[curI][curJ] == True:
                        continue
                    if heights[curI][curJ] >= heights[cur[0]][cur[1]]:
                        visited[curI][curJ] = True
                        queue.append((curI,curJ))
        pacQ = deque()
        atlQ = deque()
        for i in range(n):
            pacQ.append((0,i))
            pacVisit[0][i] = True
            atlQ.append((m - 1, i))
            atlVisit[m-1][i] = True
        for j in range(m):
            pacQ.append((j,0))
            pacVisit[j][0] = True
            atlQ.append((j,n-1))
            atlVisit[j][n-1] = True
        bfs(pacQ,pacVisit)
        bfs(atlQ,atlVisit)
        res = []
        for i in range(m):
            for j in range(n):
                if pacVisit[i][j] and atlVisit[i][j]:
                    res.append([i,j])
        return res
            

                        




        