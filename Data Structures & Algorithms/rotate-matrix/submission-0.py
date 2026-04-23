import math
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        size = len(matrix)
        if size % 2 == 0:
            m , n = size // 2,size // 2
        else:
            m = (math.ceil(size / 2))
            n = (math.floor(size / 2))
        for i in range(m):
            for j in range(n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[size - j - 1][i]
                matrix[size - j - 1][i] = matrix[size-1-i][size - j - 1]
                matrix[size-1-i][size - j - 1]= matrix[j][size - i - 1]
                matrix[j][size - i - 1]= temp


                
        
        