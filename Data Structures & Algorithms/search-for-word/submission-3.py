class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        wordLen = len(word)
        m , n = len(board), len(board[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        def dfs(wordIndex, i,j):
            if board[i][j] != word[wordIndex] :
                return False
            if wordLen == wordIndex + 1:
                return True
            visited[i][j] = True
            for di,dj in directions:
                curI, curJ = di + i, dj + j
                if curI < 0 or curI >= m or curJ < 0 or curJ >= n or visited[curI][curJ]:
                    continue
                if dfs(wordIndex + 1, curI,curJ):
                    return True
            visited[i][j] = False
            return False     
        for i in range(m):
            for j in range(n):
                if dfs(0,i,j):
                    return True
        return False      
        