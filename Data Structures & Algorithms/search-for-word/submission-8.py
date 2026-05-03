class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        n = len(word)
        self.res = False
        used = set()
        def dfs(index : int, i : int, j : int):
            if self.res == True:
                return
            if board[i][j] != word[index]:
                return
            used.add((i, j))
            for x, y in directions:
                curI = i + x 
                curJ = j + y
                if index + 1 == n:
                    self.res = True
                if curI < 0 or curJ < 0 or curI >= len(board) or curJ >= len(board[0]) or (curI, curJ) in used:
                    continue
                dfs(index + 1, curI, curJ)
            used.remove((i, j))
        for i in range(len(board)):
            if self.res:
                break
            for j in range(len(board[0])):
                if self.res:
                    break
                dfs(0, i, j)
        return self.res            
        