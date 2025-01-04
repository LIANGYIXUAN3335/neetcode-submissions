from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # solution 1 bfs from all the 0 node near the edge of the board
        # m = len(board)
        # n = len(board[0])
        # directions = [(1,0),(0,1),(-1,0),(0,-1)]
        # def bfs(queue):
        #     while queue:
        #         cur = queue.popleft()
        #         board[cur[0]][cur[1]] = "T"
        #         for di, dj in directions:
        #             curI,curJ = di + cur[0], dj + cur[1]
        #             if curI < 0 or curJ < 0 or curI >= m or curJ >= n :
        #                 continue
        #             if board[curI][curJ] == 'O':
        #                 queue.append((curI,curJ))
        # queue = deque()
        # for i in range(m):
        #     if board[i][0] == 'O':
        #         queue.append((i,0))
        #     if board[i][n - 1] == 'O':
        #         queue.append((i,n-1))
        # for j in range(1,n-1):
        #     if board[0][j] == 'O':
        #         queue.append((0,j))
        #     if board[m-1][j] == 'O':
        #         queue.append((m-1,j))
        # bfs(queue)
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == 'T':
        #             board[i][j] = 'O'
        #         elif board[i][j] == 'O':
        #             board[i][j] = 'X'
                    


        # solution 2 dfs from all the 0 node near the edge of the board
        m = len(board)
        n = len(board[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(i,j):
            board[i][j] = "T"
            for di, dj in directions:
                curI,curJ = di + i, dj + j
                if curI < 0 or curJ < 0 or curI >= m or curJ >= n :
                    continue
                if board[curI][curJ] == 'O':
                    dfs(curI,curJ)
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][n - 1] == 'O':
                dfs(i,n-1)
        for j in range(1,n-1):
            if board[0][j] == 'O':
                dfs(0,j)
            if board[m-1][j] == 'O':
                dfs(m-1,j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        # solution 3 dsu union all the 0 node near the edge of the board