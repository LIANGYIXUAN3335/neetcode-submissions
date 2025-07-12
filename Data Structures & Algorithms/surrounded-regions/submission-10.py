class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(i : int, j : int):
            board[i][j] = "#"
            for x, y in directions:
                curI, curJ =  i+ x, j + y
                if curI <0 or curJ< 0 or curI >= m or curJ >=n or board[curI][curJ] != 'O':
                    continue
                dfs(curI, curJ)
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n - 1] == 'O':
                dfs(i, n - 1)
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0,j)
            if board[m - 1][j] == 'O':
                dfs(m - 1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
    
        