class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.rowMap = [[False] * 9 for _ in range(9)]
        self.colMap = [[False] * 9 for _ in range(9)]
        self.boardMap = [[False] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != "." :
                    curNum = int(board[i][j]) 
                    if not self.isValid(i , j , curNum):
                        return False
                    self.rowMap[i][curNum - 1] = True
                    self.colMap[j][curNum - 1] = True
                    self.boardMap[( i // 3) * 3 + j // 3][curNum - 1] = True
        return True

    


    def isValid(self, i : int ,j : int, num : int) -> bool:
        if  self.rowMap[i][num - 1]:
            return False
        if  self.colMap[j][num - 1]:
            return False
        if  self.boardMap[ (i // 3) * 3 + j // 3][num - 1]:
            return False
        return True
    
        