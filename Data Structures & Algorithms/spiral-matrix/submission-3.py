class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        top , bottom = 0, n-1
        m = len(matrix[0])
        left, right = 0 , m -1
        res = []
        while left <= right and top <= bottom:
            print(left,right,top,bottom)
            for i in range(right - left + 1):
                res.append(matrix[top][left + i])
            top += 1
            for i in range(bottom - top + 1):
                res.append(matrix[top + i][right])
            right -= 1
            if top <= bottom:
                for i in range(right - left + 1):
                    res.append(matrix[bottom][right - i])
                bottom -= 1
            if right >= left:
                for i in range(bottom - top + 1):
                    res.append(matrix[bottom - i][left]) 
                left += 1          
        return res