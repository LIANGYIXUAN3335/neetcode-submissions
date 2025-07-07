class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificSet = set()
        atlanticSet = set()
        res = []
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        m = len(heights)
        n = len(heights[0])
        for i in range(m):
            pacificSet.add((i,0))
            atlanticSet.add((i, n - 1))
        for j in range(n):
            pacificSet.add((0,j))
            atlanticSet.add((m - 1, j))
        def dfs(i, j, pacOrAtlan):
            for x, y in directions:
                curI, curJ = i + x, j + y
                if curI < 0 or curJ < 0 or curI >=m or curJ >= n or heights[curI][curJ] < heights[i][j] :
                    continue
                if pacOrAtlan :
                    if (curI, curJ) in pacificSet:
                        continue
                    pacificSet.add((curI, curJ))
                    dfs(curI, curJ, True)
                else:
                    if (curI, curJ) in atlanticSet:
                        continue
                    atlanticSet.add((curI, curJ))
                    dfs(curI, curJ, False)
        for i , j in list(pacificSet):
            dfs(i,j, True)
        for i , j in list(atlanticSet):
            dfs(i, j, False)
        for i, j in pacificSet:
            if (i,j) in atlanticSet:
                res.append((i,j))
        return res
            
            