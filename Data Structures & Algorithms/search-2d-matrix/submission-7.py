class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        startI , startJ = 0, n - 1
        while startI < m and startJ >=0:
            if matrix[startI][startJ] > target:
                startJ -= 1
            elif matrix[startI][startJ] == target:
                return True
            else:
                startI += 1
        return False


        