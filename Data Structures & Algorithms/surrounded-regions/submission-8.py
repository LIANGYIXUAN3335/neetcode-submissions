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
        # def dfs(i,j):
        #     board[i][j] = "T"
        #     for di, dj in directions:
        #         curI,curJ = di + i, dj + j
        #         if curI < 0 or curJ < 0 or curI >= m or curJ >= n :
        #             continue
        #         if board[curI][curJ] == 'O':
        #             dfs(curI,curJ)
        # for i in range(m):
        #     if board[i][0] == 'O':
        #         dfs(i,0)
        #     if board[i][n - 1] == 'O':
        #         dfs(i,n-1)
        # for j in range(1,n-1):
        #     if board[0][j] == 'O':
        #         dfs(0,j)
        #     if board[m-1][j] == 'O':
        #         dfs(m-1,j)
        dsu = DSU(m * n)      
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if i ==0 or j ==0 or i == m-1 or j == n-1:
                        dsu.union(m * n,  i * n + j)
                    else:
                        for dx, dy in directions:
                            ni,nj = i + dx, j + dy
                            if board[ni][nj] == 'O':
                                dsu.union(i * n + j , ni * n + nj)
        for i in range(m):
            for j in range(n):
                if dsu.connected(i * n + j, n * m) == False:
                    board[i][j] = 'X'
                        
                        

        # solution 3 dsu union all the 0 node near the edge of the board
class DSU:
    def __init__(self,n):
        self.Parents = [i for i in range(n + 1)]
        self.Size = [1 for i in range(n + 1)]
    def findParent(self,node):
        if self.Parents[node] != node:
            self.Parents[node] = self.findParent(self.Parents[node])
        return self.Parents[node]
    def union(self,node1,node2):
        root1 = self.findParent(node1)
        root2 = self.findParent(node2)
        if root1 == root2:
            return 
        if self.Size[root1] >= self.Size[root2]:
            self.Size[root1] += self.Size[root2]
            self.Parents[root2] = root1
        else:
            self.Size[root2] += self.Size[root1]
            self.Parents[root1] = root2
    def connected(self,node1,node2):
        root1 = self.findParent(node1)
        root2 = self.findParent(node2)
        if root1 == root2:
            return True
        return False
